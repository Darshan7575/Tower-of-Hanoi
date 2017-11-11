n=int(input("Enter the number of rings in the source peg\n"))
source=list()
for i in range(n):
    source.append(n-i)
dest=list()
aux=list()
def change(source,destination):
    destination.append(source[-1])
    source.remove(source[-1])
    return source,destination
for i in range(1,2**n):
    if i%3==2 and n%2!=0:
        if len(source)==0:
            print("Move ring %d from X to S"%aux[-1])
            aux,source=change(aux,source)
        elif len(aux)==0:
            print("Move ring %d from S to X"%source[-1])
            source,aux=change(source,aux)
        elif source[-1]>aux[-1]:
            print("Move ring %d from X to S"%aux[-1])
            aux,source=change(aux,source)
        else:
            print("Move ring %d from S to X"%source[-1])
            source,aux=change(source,aux)
    elif i%3==2 :
        if len(source) == 0:
            print("Move ring %d from D to S" % dest[-1])
            dest, source = change(dest, source)
        elif len(dest) == 0:
            print("Move ring %d from S to X" % source[-1])
            source, dest = change(source, dest)
        elif source[-1] > dest[-1]:
            print("Move ring %d from D to S" % dest[-1])
            dest, source = change(dest, source)
        else:
            print("Move ring %d from S to D" % source[-1])
            source, dest = change(source, dest)
    elif i%3==1 and n%2!=0:
        if len(source)==0:
            print("Move ring %d from D to S"%dest[-1])
            dest,source=change(dest,source)
        elif len(dest)==0:
            print("Move ring %d from S to D"%source[-1])
            source,dest=change(source,dest)
        elif source[-1]>dest[-1]:
            print("Move ring %d from D to S"%dest[-1])
            dest,source=change(dest,source)
        else:
            print("Move ring %d from S to D"%source[-1])
            source,dest=change(source,dest)
    elif i%3==1:
        if len(source) == 0:
            print("Move ring %d from X to S" % aux[-1])
            aux, source = change(aux, source)
        elif len(aux) == 0:
            print("Move ring %d from S to X" % source[-1])
            source, aux = change(source, aux)
        elif source[-1] > aux[-1]:
            print("Move ring %d from X to S" % aux[-1])
            aux, source = change(aux, source)
        else:
            print("Move ring %d from S to X" % source[-1])
            source, aux = change(source, aux)
    else:
        if len(dest)==0:
            print("Move ring %d from X to D"%aux[-1])
            aux,dest=change(aux,dest)
        elif len(aux)==0:
            print("Move ring %d from D to X"%dest[-1])
            dest,aux=change(dest,aux)
        elif dest[-1]>aux[-1]:
            print("Move ring %d from X to D"%aux[-1])
            aux,dest=change(aux,dest)
        else:
            print("Move ring %d from D to X"%dest[-1])
            dest,aux=change(dest,aux)
