def area(points):
  #points -> List[List] -> [[0,1], [2,3], [3,4]]
  points.append(points[0])
  lsum = 0
  rsum = 0
  for i in range(len(points)-1):
    lsum += points[i][0] * points[i+1][1]
    rsum += points[i][1] * points[i+1][0]
  return(abs(0.5*(lsum - rsum)))
