import operator as op

nbs = [9,5,2,10,50,15,7]

operations = {op.add: '+',
              op.sub: '-',
              op.mul: '*',
              op.truediv: '/'}
target = 97

def lceb(nbs, target, path, counter):
    
    for i in range(len(nbs)):
        for j in range(i+1, len(nbs)):
            for ope in [op.add, op.sub, op.mul, op.truediv]:
                res = ope(nbs[i], nbs[j])
                
                if int(res) == res and res > 0:
                    
                    res = int(res)
                    target -= res
                    
                    if target == 0:
                        path.append(f"{nbs[i]} {operations[ope]} {nbs[j]}")
                        print(target, nbs, path)
                        print("FOUND !")
                        target += res
                        path.pop()
                        return
                    
                    if target < 0:
                        target += res
                        continue
                    
                    new_nbs = nbs[:i] + nbs[i+1:j] + nbs[j+1:]
                    new_nbs.append(res)
                    new_nbs.sort(reverse = True)
                    
                    path.append(f"{nbs[i]} {operations[ope]} {nbs[j]}")
                    #print(target, new_nbs, path)
                    
                    if len(new_nbs) == 1:
                        new_nbs.pop()
                        path.pop()
                        new_nbs.append(nbs[i])
                        new_nbs.append(nbs[j])
                        target += res
                    else:
                        if counter < 1000:
                            lceb(new_nbs, target, path, counter + 1)
                    

counter = 0
path = []
nbs.sort(reverse = True)
lceb(nbs, target, path, counter)