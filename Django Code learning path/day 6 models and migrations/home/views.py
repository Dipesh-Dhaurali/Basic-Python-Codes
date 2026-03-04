from django.shortcuts import render


def home(request):
    #Note that only context pass is possible to html only dictionary
    peoples=[
        {"name":"Dipesh Dhaurali" , "age":22},
        {"name":"Krtika Dangi" , "age":21},
        {"name":"Dipa Dhaurali" , "age":16},
        {"name":"Rekha Upreti" , "age":30},
        {"name":"Dipendra Dhaurali" , "age":40},
        {"name":"Raju Shrestha" , "age":12}
    ]
    context={"context":peoples , "title":"Ecom Site"}
    return render(request,"index.html",context)



def about(request):
    skills=['python','php','django','sql']
    context={"context":skills , "title":"aboutus"}
    return render(request,"aboutus.html",context)


def contact(request):
    context={"title":"contactus"}
    return render(request,"contactus.html",context)


