from django.shortcuts import render,redirect
from django.urls import reverse
from books.models import Book,Borrow,Comment
from books.forms import CommentForm
from django.utils import timezone
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string


def book_details(request,id):
    book=Book.objects.get(pk=id)

    #handel comment
    if request.user.is_authenticated:
        if request.method=='POST':
            form=CommentForm(request.POST)
            if form.is_valid():
                new_form=form.save(commit=False)
                new_form.book=book
                new_form.name=request.user.first_name
                new_form.save()
    form=CommentForm()
    if request.user.is_authenticated:
        is_borrow=Borrow.objects.filter(book=book,account=request.user.account).first()
    else:
        is_borrow=None
    
    comments=Comment.objects.filter(book=book)
    return render(request,'books/book_details.html',{'book':book,"form":form,'is_borrow':is_borrow,'comments':comments})

@login_required
def borrow_book(request,id):
    book=Book.objects.get(pk=id)
    bro_price=book.borrowing_price
    account=request.user.account
    balance=account.balance
    if(balance>bro_price):
        account.balance-=bro_price
        account.save()
        Borrow.objects.create(
            book=book,
            account=account,
            borrow_after_price=balance-bro_price
        )

        # send email
        mail_subject="Borrow Book Message"
        to_mail=request.user.email
        message=render_to_string('books/borrow_mail.html',{"book":book,"balance":balance})
        send_email=EmailMultiAlternatives(mail_subject,'',to=[to_mail])
        send_email.attach_alternative(message,'text/html')
        send_email.send()
        messages.success(request,"Borrowing success")
    else:
        messages.warning(request,"Your account has not available balance")
    return redirect(reverse('book_details', args=[id]))

@login_required
def return_book(request,id):
    borrow_return=Borrow.objects.get(pk=id)
    amount=borrow_return.book.borrowing_price
    account=request.user.account
    account.balance+=amount
    account.save()
    borrow_return.delete()
    messages.success(request,"Book return successfully")
    return redirect("profile")

