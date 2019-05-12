def my_map(exp, Iterable):
  if len(Iterable) == 0:
    return []
  return [exp(Iterable[0])] +  my_map(exp, Iterable[1:])

def my_tail_map(exp, Iterable, result = []):
  if 0 == len(Iterable):
    return result
  return my_tail_map(exp, Iterable[1:], result + [exp(Iterable[0])])

def add3dicts(d1, d2, d3):
  Help = list(set(list(d1) + list(d2) + list(d3)))
  Help2 = my_tail_map(lambda x: my_append(x, d1, d2, d3), Help)
  return dict(zip(Help, Help2))

def my_append(x, d1, d2, d3):
  if x in d1 and x in d2 and x in d3:
    return tuple([d1[x],d2[x],d3[x]])
  if x in d1 and x in d2:
    return tuple([d1[x],d2[x]])
  if x in d1 and x in d3:
    return tuple([d1[x], d3[x]])
  if x in d2 and x in d3:
    return tuple([d2[x], d3[x]])
  if x in d1:
    return d1[x]
  if x in d2:
    return d2[x]
  if x in d3:
    return d3[x]

def input3dictsAndMarge():
    print(add3dicts(eval(input("Enter the first dict:\n>")),eval(input("Enter the second dict:\n>")),eval(input("Enter the 3 dict:\n>"))))

if __name__ == "__main__":
    input3dictsAndMarge()
