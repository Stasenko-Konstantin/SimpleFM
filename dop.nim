import nimpy

proc sortdir*(arg: seq[string]): seq[string] {.exportpy.} =
  var
    x1 = @[""]
    x2 = @[""]
  for i in arg:
    echo i
    if '.' in i:
      x2.add(i)
    else:
      x1.add(i)
  result = x1[1..x1.len-1] & x2[1..x2.len-1]

proc concat*(arg: string): string {.exportpy.} =
  return arg & "//"

proc concat2*(arg: string): string {.exportpy.} = 
  return "//" & arg

proc str_to_list*(arg: string): seq[string] {.exportpy.} =
  result = @[]
  for i in arg:
    result.add($i)

proc list_to_str*(arg: seq[string]): string {.exportpy.} = 
  var r = ""
  for i in arg:
    r &= i
  return r

proc reverse[T](arg: seq[T]): seq[T] = 
  if arg == @[]:
    return @[]
  else:
    return reverse(arg[1..arg.len-1]) & arg[0]

proc take_while*(arg: seq[string], spl: string): seq[string] {.exportpy.} =
  result = arg
  for i in 0..arg.len:
    if list_to_str(result[i..i+1]) == spl:
      return result[i+1..result.len-1]

proc take_while2*(arg: seq[string], spl: string): seq[string] {.exportpy.} =
  result = arg
  for i in 0..arg.len:
    if list_to_str(result[i..i+1]) == spl:
      return result[0..i+1]

proc got_back*(arg: string, spl: string): string {.exportpy.} =
  var r = str_to_list(arg).reverse()
  return list_to_str(take_while(r, spl).reverse())

proc btn_lists*(stdlist: seq[string]): seq[string] {.exportpy.} =
  result = @[]
  var name = ""
  for i in 0..stdlist.len-1:
    name = "btn" & $i
    result.add(name)