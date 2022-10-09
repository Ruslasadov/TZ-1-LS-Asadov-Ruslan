def read():
   f = open("input.txt", "r")
   return f.read()


def get_str_with_nums():
   all_strs = read().split('\n')
   strs = {}
   for str in all_strs:
    strs[str] = all_strs.count(str)
   return strs



def write(strs):
   data = dict(sorted(strs.items(), key=lambda item: item[1]))
   f = open("output.txt", "w")
   for term, key in data.items():
      f.write(f"{term}\t{key}\n")
   f.close()

if __name__ == '__main__':
   write(get_str_with_nums())
