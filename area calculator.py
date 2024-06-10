import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sympy import *
import math
from fractions import Fraction
print("WELCOME TO MATHSOLVER")
print("THESE ARE THE FUNCTIONS WE CAN SOLVE ")
df=pd.read_csv("functions.csv")
print(df)
print("TYPE STOP TO STOP THE FUNCTION AND TYPE STOP AGAIN TO STOP THE PROGRAMME !!")
print("ENTER THE SERIAL NUMBER OF THE FUNCTION YOU WANT TO PERFORM:")
while True:
  function=input().lower()
  if   function=="1":
    while True:
      print("PLEASE ENTER THE NAME OF FIGURE EXAMPLE:SQUARE,RECTANGLE ETC...")
      print("TYPE STOP TO STOP THE FUNCTION AND TYPE STOP AGAIN TO STOP THE PROGRAMME!!")
      fig=input().lower()
      if fig=="square":
        print("ENTER THE SIDE OF THE SQUARE= ")
        side=input().lower()
        while True:
          if side.isdigit():
            s=int(side)
            area=s**2
            print("AREA OF THE SQUARE IS",area,"sq.units")
            break
          elif side=="stop":
            print("ENTER A NUMBER")
          else:
            print("PLEASE ENTER AN INTEGER!!")
            break
            
      elif fig=="rectangle":
        print("ENTER THE LENGTH:")
        lr=input().lower()
        print("ENTER THE BREADTH:")
        br=input().lower()
        while True:
          if lr.isdigit() and br.isdigit():
            l=int(lr)
            b=int(br)
            area=l*b
            print("AREA OF THE RECTANGLE IS",area,"sq.units")
            break
          elif lr=="stop" or br=="stop":
            print("ENTER A NUMBER")
          else:
            print("PLEASE ENTER AN INTEGER!!")
            break
        
      elif fig=="triangle":
        print("ENTER THE BASE OF TRIANGLE")
        bt=input().lower()
        print("ENTER THE HEIGHT OF TRIANGLE")
        ht=input().lower()
        while True:
          if bt.isdigit() and ht.isdigit():
            b=int(bt)
            h=int(ht)
            area=(b+h)/2
            print("AREA OF THE TRIANGLE IS",area,"sq.units")
            break
          elif bt=="stop" or ht=="stop":
            print("ENTER A NUMBER")
          else:
            print("PLEASE ENTER AN INTEGER!!")
            break
            
      elif fig=="parallelogram":
        print("ENTER THE BASE:")
        bp=input().lower()
        print("ENTER THE HEIGHT:")
        hp=input().lower()
        while True:
          if bp.isdigit() and hp.isdigit():
            bp=int(bp)
            hp=int(hp)
            print("THE AREA OF PARALLALOGRAM IS ",bp*hp,"sq.units")
            break
          elif bp=="stop" or hp=="stop":
            print("ENTER A NUMBER")
          else:
            print("PLEASE ENTER AN INTEGER!!")
            break
      elif fig=="circle":
         print("ENTER THE RADIUS OF CIRCLE :")
         rc=input().lower()
         while True:
            if rc.isdigit():
             rc=int(rc)
             print("THE AREA OF CIRCLE IS",3.1415*rc*rc,"sq.units")
             break
            elif rc =="stop":
              print("ENTER A NUMBER")
            else:
              print("PLEASE ENTER AN INTEGER!!")
              break
              
      elif fig=="trapezium":
        print("ENTER THE BASE-1")
        b1t=input().lower()
        print("ENTER THE BASE-2")
        b2t=input().lower()
        print("ENTER THE HEIGHT ")
        htp=input().lower()
        while True:
          if (b1t.isdigit() and b2t.isdigit() and htp.isdigit()):
            b1t=int(b1t)
            b2t=int(b2t)
            htp=int(htp)
            print("THE AREA OF TRAPEZIUM IS",((b1t+b2t)*htp)/2,"sq.units")
            break
          elif b1t=="stop" or b2t=="stop" or htp=="stop":
            print("ENTER A NUMBER")
          else:
              print("PLEASE ENTER AN INTEGER!!")
              break
      elif fig=="cylinder":
         print("ENTER THE RADIUS")
         rcr=input().lower()
         print("ENTER THE HEIGHT ")
         hcr=input().lower()
         while True:
            if rcr.isdigit() and hcr.isdigit():
             rcr=int(rcr)
             hcr=int(hcr)
             print("THE TOTAL SURFACE AREA OF CYLINDER IS ",6.283*rcr*(rcr+hcr),"sq.units")
             break
            elif rcr=="stop" or hcr=="stop":
              print("ENTER A NUMBER")
            else:
              print("PLEASE ENTER AN INTEGER!!")
              break
              
      elif fig=="ellipse":
         print("ENTER THE MAJOR AXIS:")
         mje=input().lower()
         print("ENTER THE MINOR AXIS:")
         mne=input().lower()
         while True:
            if mje.isdigit() and mne.isdigit():
             mje=int(mje)
             mne=int(mne)
             print("THE AREA OF ELLIPSE IS",3.1415*(mje/2)*(mne/2),"sq.units")
             break
            elif mje=="stop" or mne=="stop":
              print("ENTER A NUMBER")
            else:
              print("PLEASE ENTER AN INTEGER!!")
              break
              
      elif fig=="cube":
          print("ENTER THE SIDE:")
          sc=input().lower()
          while True:
            if sc.isdigit():
              sc=int(sc)
              print("THE TOTAL SURFACE AREA OF CUBE IS ",6*sc*sc,"sq.units")
              break
            elif sc=="stop":
              print("ENTER A NUMBER")
            else:
              print("PLEASE ENTER AN INTEGER!!")
              break
              
      elif fig=="cone":
         print("ENTER THE RADIUS")
         rc=input().lower()
         print("ENTER THE HEIGHT")
         hc=input().lower()
         while True:
            if rc.isdigit() and hc.isdigit():
             rc=int(rc)
             hc=int(hc)
             shc=math.sqrt(hc*2+rc*2)
             print("THE AREA OF CONE IS",3.1415*rc*(rc+shc),"sq.units")
             break
            elif rc=="stop" or hc=="stop":
              print("ENTER A NUMBER")
            else:
              print("PLEASE ENTER AN INTEGER!!")
              break
      elif fig=="sphere":
        print("ENTER THE RADIUS")
        rsp=input().lower()
        while True:
          if rsp.isdigit():
            rsp=int(rsp)
            print("THE AREA OF SPHERE IS",4*3.1415*rsp*rsp,"sq.units")
            break
          elif rsp=="stop":
            print("ENTER A NUMBER")
          else:
              print("PLEASE ENTER AN INTEGER!!")
              break
            
      elif fig=="hemisphere":
         print("ENTER THE RADIUS:")
         rhs=input().lower()
         while True:
            if rhs.isdigit():
             rhs=int(rhs)
             print("THE AREA OF HEMISPHERE IS ",3*3.1415*rhs*rhs,"sq.units")
             break
            elif rhs=="stop":
              print("ENTER A NUMBER")
            else:
              print("PLEASE ENTER AN INTEGER!!")
              break
      elif fig=="rectangular prism":
         print("ENTER THE LENGTH:")
         lrt=input().lower()
         print("ENTER THE WIDTH:")
         wrt=input().lower()
         print("ENTER THE HEIGHT:")
         hrt=input().lower()
         while True:
            if lrt.isdigit() and wrt.isdigit() and hrt.isdigit():
             lrt=int(lrt)
             wrt=int(wrt)
             hrt=int(hrt)
             atrp=(wrt*lrt)+(hrt*lrt)+(hrt*wrt)
             print("THE AREA OF RECTANGULAR TRAPEZIUM IS",2*atrp,"sq.units")
             break
            elif lrt=="stop" or wrt=="stop" or hrt=="stop":
              print("ENTER A NUMBER")
            else:
              print("PLEASE ENTER AN INTEGER!!")
              break
      elif fig=="rhombous":
        s1=input("ENTER THE DIAGONAL 1:").lower()
        s2=input("ENTER THE DIAGONAL 2:").lower()
        while True:
          if s1.isdigit() and s2.isdigit():
           s1=int(s1)
           s2=int(s2)
           print("THE AREA OF RHOMBOUS IS:",(1/2)*(s1*s2))
           break
          elif s1=="stop" or s2=="stop":
            print("ENTER A NUMBER")
          else:
              print("PLEASE ENTER AN INTEGER!!")
              break
      elif fig=="kite":
        e1=input("ENTER THE DIAGONAL 1:").lower()
        e2=input("ENTER THE DIAGONAL 2:").lower()
        while True:
          if e1.isdigit() and e2.isdigit():
            e1=int(e1)
            e2=int(e2)
            print("THE AREA OF KITE IS:",(1/2)*(e1*e2))
            break
          elif e1=="stop" or e2=="stop":
            print("ENTER A NUMBER")
          else:
              print("PLEASE ENTER AN INTEGER!!")
              break
      elif fig=="semi circle" or fig=="semicircle":
        rs=input("ENTER RADIUS OF THE CIRCLE:").lower()
        while True:
          if rs.isdigit():
            rs=int(rs)
            print("AREA OF SEMI CIRCLE IS",((1/2)*(3.1415*rs)))
            break
          elif rs=="stop":
            print("ENTER A NUMBER")
          else:
              print("PLEASE ENTER AN INTEGER!!")
              break
      elif fig=="sector":
        sa=input("ENTER THE ANGLE OF THE SECTOR(IN DEGREES):").lower()
        while True:
          if sa.isdigit():
            sa=int(sa)
            print("AREA OF THE SECTOR IS",sa/360)
            break
          elif sa=="stop":
            print("ENTER A NUMBER")
          else:
              print("PLEASE ENTER AN INTEGER!!")
              break
      elif fig=="stop":
        print("STOPPING THE PROGRAMME")
        break
      else:
        print("SORRY WE DONOT HAVE THAT VALUE")
        pr=pd.read_csv("areas.csv")
        print(pr)
        print("PLEASE SELECT THE FIGURE FROM THE ABOVE DATA")
    
  elif function=="3":
    while True:
      print("NOTE : THE QUADRATIC EQUATION OF FORM ax^2+bx+c CAN ONLY BE FOUND IN THIS PROGRAMME.TYPE OK IF YOU AGREE WITH IT")
      print("TYPE STOP TO STOP THE FUNCTION AND TYPE STOP AGAIN TO STOP THE PROGRAMME!!")
      user=input().upper()
      if "OK" in user:
        print("WELCOME")
        print("ENTER THE VALUE OF a:")
        va=input().lower()
        print("ENTER THE VALUE OF b:")
        vb=input().lower()
        print("ENTER THE VALUE OF c:")
        vc=input().lower()
        while True:
          if va.isdigit() and vb.isdigit() and vc.isdigit():
            va=int(va)
            vb=int(vb)
            vc=int(vc)
            eq1=(vb**2)-(4*va*vc)
            eq2=(eq1)(1/2)
            eq3=(-vb+eq2)/2*va
            eq4=(-vb-eq2)/2*va
            print("THE ROOTS OF THE GIVEN QUADRATIC EQUATION ARE",eq3,eq4)
            if eq1>=0:
             print("CONGRATS ,THESE ROOTS ARE REAL ROOTS :)")
            else:
             print("OHH LOOKS LIKE THESE ARE  IMAGINARY ROOTS :)")
             break
          elif va=="stop" or vb=="stop" or vc=="stop":
              print("ENTER A NUMBER")
          else:
              print("PLEASE ENTER AN INTEGER!!")
              break
      elif "stopf" in user:
        break
      else:
        print("SORRY ,WE COULD'NT GET THAT!!")
  elif function=="2":
    while True:
      print("ENTER THE TRIGNOMETRIC FUNCTION YOU WANT TO PERFORM.(example:cos(x),sin(x))")
      print("TYPE STOP TWO TIMES TO STOP THE PROGRAMME AFTER COMPLETING")
      trin=input().lower()
      print("ENTER THE ANGLE(x) IN RADIANS:")
      teta=input()
      while True:
        if (trin.isalpha()):
          if "sin(x)" in trin:
             print(math.sin(teta))
          elif "cos(x)" in trin:
             print(math.cos(teta))
          elif "tan(x)" in trin:
             print(math.tan(teta))
          elif "cot(x)" in trin:
             print(math.cot(teta))
          elif "cosec(x)" in trin:
             print(math.cosec(teta))
          elif "sec(x)" in trin:
             print(math.sec(teta))
          elif "arcsin(x)" in trin:
             print(math.asin(teta))
          elif "arccos(x)" in trin:
             print(math.acos(teta))
          elif "arccosec(x)" in trin:
            print(math.arccosec(teta))
          elif "arctan(x)" in trin:
              print(math.atan(teta))
          elif "arcsec(x)" in trin:
              print(math.asec(teta))
          elif trin=="stop":
             break
        elif trin=="stop" or teta=="stop":
          break
        elif teta.isalpha():
          print("PLEASE ENTER THE VALUE OF ANGLE IN RADIANS")
          break
        else:
          print("WE DO NOT HAVE THE VALUE YOU ENTERED. PLEASE SELECT ONE FROM THE BELOW.")
          tr=pd.read_csv("trigonometry.csv")
          print(tr)
          break
  elif function=="5":
    while True:
      print("IN THIS YOU CAN ONLY GET THE PARTICULAR LOGARITHRM FUNCTION EXAMPLE:LOG2 ,ETC... TYPE YES IF YOU AGREE :)")
      print("TYPE STOP TWO TIMES TO STOP THE PROGRAMME AFTER COMPLETING")
      agree=input().lower()
      if agree=="yes":
        print("ENTER THE VALUE :")
        val=float(input())
        print("ENTER THE LOGARITHEMIC BASE:")
        base=float(input())
        if val.isdigit() and base.isdigit():
          value=math.log(val,base)
          print("THE VALUE OF LOGARITHEM IS",value)
        elif val=="stop" or base=="stop":
          break
        else:
          print("ENTER THE VALID NUMBER")
          break
      elif agree=="stop":
          break
      else:
        print("SORRY,WE COULD'NT GET IT")
        
  elif function=="4":
    while True:
      x, y = symbols('x y')
      print("ENTER THE FUNCTION (NOTE:ENTER ANY FUNCTION CONTAINING ONLY TWO VARIABLES X AND Y AND DO NOT ENTER ANY NUMBER. THIS DIFFERENTIATION IS WITH RESPECTIVE X ONLY):")
      print("NOTE: THE X^n NEED TO BE ENTERED AS X*n AND nX NEED TO BE ENTERED AS X*n EXAMPLE:2*X*2+X+3*Y")
      print("TYPE STOP TWO TIMES TO STOP THE PROGRAMME AFTER COMPLETING")
      print("TYPE YES TO CONTINUE")
      ag=input().lower()
      if ag=="yes":
        print("ENTER THE FUNCTION")
        expr = input().lower()
        if expr.isdigit():
          expr_diff = Derivative(expr, x)
          print("THE DERIVATIVE IS :",expr_diff.doit())
        elif expr=="stop":
          break
        else:
          print("PLEASE ENTER THE VALUE CORRECTLY")
        
      elif ag=="stop":
             break
      else:
            print("SORRY,WE COULD'NT GET IT")

  elif function=="6":
    while True:
      print("YOU HAVE TO ENTER THE X AND Y AXIS POINT IN THE FUNCTION GRAPHS AND WE WILL PLOT THE GRAPH FOR YOU TYPE YES TO CONTINUE")
      print("TYPE STOP TWO TIMES TO STOP THE PROGRAMME AFTER COMPLETING")
      ag=input()
      if "yes" in ag:
        print("ENTER THE VALUES OF X AND Y IN A SINGLE LINE.EXAMPLE:1,2,3,4....")
        print("ENTER X-AXIS VALUES:")
        x=list(map(int,input().split(",")))
        x.sort()
        print("ENTER Y-AXIS VALUES:")
        y=list(map(int,input().split(",")))
        plt.plot(x,y) 
        plt.show()
        plt.close('all')
      elif "stop" in ag:
        break
      else:
        print("SORRY,WE COULD'NT GET IT :)")
  
  elif function=="7":
    while True:
      print("WHAT DO YOU WANT TO FIND PERMUTATION OR COMBINANTION TYPE P FOR PERMUTATION AND C FOR COMBINANTION:")
      print("TYPE STOP TWO TIMES TO STOP THE PROGRAMME AFTER COMPLETING")
      pc=input().lower()
      if pc=="p":
        print("ENTER THE NO.OF OBSERVATIONS (n):")
        nob=int(input())
        print("NOTE** : n MUST BE GREATER THAN r")
        print("ENTER THE CHOICE OF OBSERVATIONS(r):")
        rob=int(input())
        while True:
          if nob<rob:
            print("THE NO.OF OBSERVATIONS MUST BE GREATER THAN THE CHOICE OF OBSERVATIONS!!")
            break
          else:
            nr=math.factorial(nob)
            dr=math.factorial(nob-rob)
            print("THE PERMUTATION IS",nr/dr)
      elif pc=="c":
        print("ENTER THE NO.OF OBSERVATIONS (n):")
        nobc=int(input())
        print("NOTE** : n MUST BE GREATER THAN r")
        print("ENTER THE CHOICE OF OBSERVATIONS(r):")
        robc=int(input())
        ncr=math.factorial(nobc)
        ndr=math.factorial(nobc-robc)
        nrr=math.factorial(robc)
        print("THE COMBINANTION IS",ncr/(ndr*nrr))
      elif "stop" in pc:
        break
      else:
        print("SORRY,WE COULD'NT FIND THE WORD YOU HAVE ENTERED")
  elif function=="9":
    while True:
      print("THIS WILL CONVERT DECIMAL NUMBER INTO A FRACTION.TYPE YES TO CONTINUE AND STOP TO STOP THE PROGRAMME.")
      use=input().lower()
      if "yes" in use:
        print("ENTER THE DECIMAL:")
        dec=float(input())
        print("THE REQUIRED FRACTION IS ",Fraction(dec))
      elif "stop" in use:
        break
      else:
        print("SORRY,WE COULD'NT GET IT")
  elif function=="10":
    while True:
      print("ENTER DR TO CONVERT DEGREES TO RADIANS AND RD TO CONVERT RADIANS TO DEGREE. ")
      ans=input().lower()
      if "dr" in ans:
        dr=float(input("ENTER DEGREES HERE:"))
        zy=(3.1415/180)*dr
        print(dr,"DEGREES =",zy,"RADIANS")
      elif "rd" in ans:
        rd=float(input("ENTER RADIANS HERE:"))
        yz=(180/3.1415)*rd
        print(rd,"RADIANS=",yz,"DEGREES")
      elif "stop" in ans:
        break
      else:
        print("SORRY,WE DID'NT GET IT.")
  elif function=="11":
    while True:
      sum=0
      print("ENTER P FOR PARALLEL CIRCUIT AND S FOR SERIES CIRCUIT")
      print("ENTER STOP TO EXIT")
      res=input().lower()
      if "s" in res:
        nr=int(input("ENTER THE NUMBER OF RESISTORS: "))
        for i in range(nr):
          print("ENTER THE RESISTANCE  ")
          r=int(input())
          sum=sum+r
        print("THE EQUALENT RESISTANCE OF CIRCUIT IN SERIES IS",sum)
      elif "p" in res:
        ns=int(input("ENTER THE NUMBER OF RESISTORS: "))
        for i in range(ns):
          print("ENTER THE RESISTOR: ")
          s=int(input()) 
          sum=sum+(1/s)
        print("THE EQUIVALENT RESISTANCE IN PARALLEL CIRCUIT IS",(1/sum))
      elif "stop" in res:
        break
      else:
        print("SORRY,WE DID'NT GET IT!!!")
  elif function=="12":
    while True:  
      v1=input("ENTER THE 1ST COLOUR:").lower()
      if v1.isalpha():
        if v1=="black":   
           d1 =0
        elif v1=="brown":
          d1=1
        elif v1=="red":
          d1=2
        elif v1=="orange":
          d1=3
        elif v1=="yellow":
          d1=4
        elif v1=="green":
          d1=5
        elif v1=="blue":
          d1=6
        elif v1=="violet":
          d1=7
        elif v1=="grey":
          d1=8
        elif v1=="white":
          d1=9
        else:
          print("PLEASE ENTER VALID COLOUR")
          break
      elif v1=="stop":
        break
      else:
        print("ENTER THE COLOUR NAME CORRECTLY")
      v2=input("ENTER THE COLOR VALUE 2:").lower()
      if v2.isalpha():
        if v2=="black":   
          d2 =0
        elif v2=="brown":
          d2=1
        elif v2=="red":
          d2=2
        elif v2=="orange":
          d2=3
        elif v2=="yellow":
          d2=4
        elif v2=="green":
          d2=5
        elif v2=="blue":
          d2=6
        elif v2=="violet":
          d2=7
        elif v2=="grey":
          d2=8
        elif v2=="white":
          d2=9 
        elif v2=="stop":
          break
        else:
          print("PLEASE ENTER VALID COLOUR")
          break
      m=input("ENTER THE COLOR MULTIPLIER:").lower()
      if m.isalpha():
        if m=="black":   
          d3 =0
        elif m=="brown":
          d3=1
        elif m=="red":
          d3=2
        elif m=="orange":
          d3=3
        elif m=="yellow":
          d3=4
        elif m=="green":
          d3=5
        elif m=="blue":
          d3=6
        elif m=="violet":
          d3=7
        elif m=="grey":
          d3=8
        elif m=="white":
          d3=9
        elif m=="gold":
          d3=-1
        elif m=="silver":
          d3=-2
        elif d3=="stop":
          break
        else:
          print("ENTER VALID COLOUR")
          break
      t=input("ENETR THE COLOR OF TOLERANCE:")
      if t.isaplha():
        if t=="brown":
          d4= 1
        elif t=="red":
          d4= 2
        elif t=="green":
          d4= 0.5
        elif t=="blue":
          d4= 0.25
        elif t=="violet":
          d4= 0.1
        elif t=="gold":
          d4= 5
        elif t=="silver":
          d4= 10
        elif t=="none":
          d4= 20  
        elif t=="stop":
          break
        else:
          print("PLEASE ENTER VALID COLOUR")
          break
      print("THE RESISTANCE IS",d1,d2,"*10^",d3,"TOLERANCE IS ±",d4,"Ω") 
    
  elif "stop" in function:
    break
  else:
    print("SORRY,WE COULD'NT FIND THE FUNCTION.CHECK WEATHER YOU HAVE ENTERED SERIAL NUMBER CORRECTLY!!")