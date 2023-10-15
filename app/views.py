from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .models import bill_model
from num2words import num2words


# Create your views here.
def index(request):
    # b=bill_model.objects.all()
    # b.delete()
    return render(request,'index.html')


def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('form_view')  # Redirect to a home page or another page.
    return redirect('index')

def user_logout(request):
    logout(request)
    return redirect('index')

@login_required(login_url='userlogin')
def form_view(request):
    return render(request,'form.html')

def form_submit(request):
    name=request.POST['name']
    GSTIN=request.POST['GSTIN']
    UIN=request.POST['UIN']
    date1=request.POST['date1']
    state1=request.POST['state1']
    email1=request.POST['email1']
    Buyer=request.POST['Buyer']
    adress=request.POST['adress']
    gstin=request.POST['gstin']
    state2=request.POST['state2']
    email2=request.POST['email2']
    phone=request.POST['phone']
    otherreferance=request.POST['otherreferance']
    ModeORtermsOfPayment=request.POST['ModeORtermsOfPayment']
    # date2=request.POST['date2']
    description1=request.POST['description1']
    hsn1=request.POST['hsn1']
    sac1=request.POST['sac1']
    per1=request.POST['per1']
    disc1=request.POST['disc1']
    amount1=request.POST['amount1']

    CentralTax=round(int(amount1)*(9/100),2)
    StateTax=round(int(amount1)*(9/100),2)
    Total=round(int(amount1)*(118/100),2)
    # Replace this with your desired number
    words = num2words(Total)
    tax_words=num2words(CentralTax+StateTax)
    print(words)

    print(date1)
    # print(date2)
    new_bill=bill_model(
        name=name,
        GSTIN=GSTIN,
        UIN=UIN,
        stateName1=state1,
        Email1=email1,
        Dated1=date1,
        Buyer=Buyer,
        adress=adress,
        Email2=email2,
        phone=phone,
        GSTIN2=gstin,
        stateName2=state2,
        ModeORtermsOfPayment=ModeORtermsOfPayment,
        OtherReference=otherreferance,
        # Dated2=date2,
        descriptionOfGoods=description1,
        HSN=hsn1,
        SAC=sac1,
        per=per1,
        disc=disc1,
        amount1=amount1,
        CentralTax=CentralTax,
        StateTax=StateTax,
        total_tax=CentralTax+StateTax,
        Total=Total,
        words=words,
        tax_words=tax_words
        )
    new_bill.save()
    print('success')
    return redirect('pdfdownload')

def pdf_download(request):
    data=bill_model.objects.latest('created_at')
    print(data)
    return render(request,'pdfPage.html',{'bill':data})
    # return redirect('index')

def bills(request):
    bills=bill_model.objects.all()
    return render(request,'bills.html',{'bills':bills})

def bill_view_pdf(request,i):
    data=bill_model.objects.get(InvoiceNo=i)
    print(data)
    return render(request,'pdfPage.html',{'bill':data})