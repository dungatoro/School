class Node {
    has $.val;
    has $!l = Nil;
    has $!r = Nil;

    method append (*@vals) {
        say $!val;
        for @vals -> $val {
            ($!l ~~ Nil ?? ($!l = Node.new($val)) !! $!l.append($val)) if $val <= $!val;
            ($!r ~~ Nil ?? ($!r = Node.new($val)) !! $!r.append($val)) if $val >  $!val;
        }
    }

    method Str { "{$!val}({$!l or '_'} {$!r or '_'})" }
}

my $tree = Node.new(val => 12);
$tree.append(8, 9, 3, -4, 4, 92, 62);

print $tree;
