#include "array.h"
#include<iostream>
#include<opencv2/opencv.hpp>

using namespace cv;

int main() {
  Mat I;
  I = imread("watman.jpg", IMREAD_COLOR);
  MatIterator_<Vec3b> it, end;
  for( it = I.begin<Vec3b>(), end = I.end<Vec3b>(); it != end; ++it)
  {
    (*it)[0] = arr[2][(*it)[0]][2];
    (*it)[1] = arr[1][(*it)[1]][1];
    (*it)[2] = arr[0][(*it)[2]][0];
  }
  imwrite("watman_c++.png", I);
  return 0; 
}
