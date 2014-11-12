tri n = [ (a,b,c) | c <- [1..n], b <- [1..c], a <- [1..b], a^2 + b^2 == c^2, a+b+c == n]
sols n = [(length (tri x), x) | x <- [1..n]]

fold :: (a -> b -> b) -> b -> [a] -> b
fold f u [] = u
fold f u (x:xs) = x `f` (fold f u xs)
solve = fold (+) 0 sols
