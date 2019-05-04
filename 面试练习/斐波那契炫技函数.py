__author__ = "那位先生Beer"
(lambda fn: (lambda f: f( f ))( lambda f: fn( lambda n: f( f )( n ) ) ))(
    lambda g: lambda n: 1 if n in [1, 2] else g( n - 1 ) + g( n - 2 ) )( 10 )
