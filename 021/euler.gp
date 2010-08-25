s=0; for(x=1,9999,d1=sumdiv(x,i,i)-x;if(d1>0,d2=sumdiv(d1,i,i)-d1;if(d2==x&d1!=x,print(x);print(d1);s+=(x)))); print(s);
