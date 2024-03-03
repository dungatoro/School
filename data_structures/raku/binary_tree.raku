class Node {
    has $.n;
    has $!l = Nil;
    has $!r = Nil;

    method append (*@vals) {
        for @vals -> $n {
             if $n <= $!n {
                if $!l.defined { 
                    $!l.append($n);
                } else {
                    $!l = Node.new(n => $n);
                }
            } elsif $n >  $!n {
                if $!r.defined {
                    $!r = Node.new(n => $n);
                } else {
                    $!r.append($n);
                }
            }
        }
    }

    method Str { 
        "{$!n}({$!l.defined ?? $!l !! '_'} {$!r.defined ?? $!r !! '_'})" 
    }
}

my $tree = Node.new(n => 12);
$tree.append(8, 9, 3, -4, 4, 92, 62);

print $tree;
