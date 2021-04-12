#determines if a point lies in a polygon

#O(1) 
def isLess(point, segment):
  xc = []
  yc = []
  for i in segment:
    xc.append(i[0])
    yc.append(i[1])
  m = (yc[1] - yc[0]) / (xc[1] - xc[0])
  c = yc[0] - m*xc[0]
  if m>0:
    return(point[1] > m*point[0] + c)
  else:
    return(point[1] < m*point[0] + c)

def intersect(point, segment):
  xc = []
  yc = []
  for i in segment:
    xc.append(i[0])
    yc.append(i[1])
  if point[1] > min(yc) and point[1] < max(yc) and isLess(point,segment):
    return True
  return False


#O(n)
def inPolygon(point, points):
  print(point)
  #ASSUMING POINT DOES NOT LIE ON POINTS
  #point [List] -> []
  #points [List[List]] -> [[],[],[],[],[]]
  #ray algorithm
  #increment count if line with slope 0 passing thru point crosses a line segment in polynomial
  #Segment = [[[],[]],[[]],[]], . . .]
  segments = []
  points.append(points[0])
  for iter in range(len(points)-1):
    segments.append([points[iter],points[iter+1]])
  count = 0
  for i in range(len(segments)):
    if intersect(point, segments[i]):
      count+=1
      print(segments[i])
  print(count)
  return(count&1 == 1)
