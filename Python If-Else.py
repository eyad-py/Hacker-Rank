{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#!/bin/python\n",
    "\n",
    "import math\n",
    "import os\n",
    "import random\n",
    "import re\n",
    "import sys\n",
    "\n",
    "\n",
    "\n",
    "if __name__ == '__main__':\n",
    "    n = int(input().strip())\n",
    "    if n>=1 and n<=100:      \n",
    "        if n % 2 !=0:\n",
    "            print('Weird')\n",
    "        elif n%2 ==0 and (n>=2 and n<=5):\n",
    "            print('Not Weird')\n",
    "        elif n%2 ==0 and (n>=6 and n<=20):\n",
    "            print('Weird')\n",
    "        elif n%2 ==0 and n>20:\n",
    "            print('Not Weird')\n",
    "        \n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
