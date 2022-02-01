from django.shortcuts import render

# Create your views here.
def create(request,n):
   divisors_list=[]
   n =int(n)
   for i in range(1,n):
       if n%i == 0:
           divisors_list.append(i)

   return render(request,'create.html',context={'divisors':divisors_list})

def divisor_sum(n):
	if n == 1:
		return 0
	else:
		res_sum = 0
		for i in range(1,n):
			if n % i == 0:
				res_sum += i
		return res_sum
def check(request,a,b):

    perfect_list = [i for i in range(a, b + 1) if i == divisor_sum(i)]
    abundant_list = [i for i in range(a, b + 1) if i > divisor_sum(i)]
    deficient_list = [i for i in range(a, b + 1) if i < divisor_sum(i)]
    return render(request,'check.html',context={'perfect':perfect_list,'abundant':abundant_list,'deficient':deficient_list})

