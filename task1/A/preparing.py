import json
import sys


if __name__ == '__main__':
  print('Start generate index.h')
  with open('index.h', 'w') as fp:
    fp.write('''
#include <iostream>


class Index {
 public:
  Index() {
   std::cout << "Index created" << std::endl;
  }
};


''')
  print('Generation finished')

