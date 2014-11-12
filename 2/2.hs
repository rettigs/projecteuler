fibs = 1:1:zipWith (+) fibs (tail fibs)
evenfibssum = sum $ takeWhile (<4000000) [ x | x <- fibs, even x]
