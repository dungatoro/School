class Node {
    has $.n;
    has $!l = Nil;
    has $!r = Nil;

    method Str{"{$!n}({$!l.defined??$!l!!'_'} {$!r.defined??$!r!!'_'})"}

    method append (*@vals) {
        for @vals -> $n {
             if $n <= $!n {
                $!l.append($n) if $!l.defined;
                $!l = Node.new(n=>$n) if not $!l.defined;
            } else {
                $!r.append($n) if $!r.defined;
                $!r = Node.new(n=>$n) if not $!r.defined;
            }
        }
    }

    method height {
        my $l-depth = $!l.defined ?? $!l.height !! 0;
        my $r-depth = $!r.defined ?? $!r.height !! 0;
        $l-depth > $r-depth ?? $l-depth+1 !! $r-depth+1
    }

    method pre-order {
        flat($!n,$!l.defined??$!l.pre-order!!(),$!r.defined??$!r.pre-order!!())
    }

    method in-order {
        flat($!l.defined??$!l.in-order!!(),$!n,$!r.defined??$!r.in-order!!())
    }

    method post-order {
        flat($!l.defined??$!l.post-order!!(),$!r.defined??$!r.post-order!!(),$!n)
    }
}

my $tree = Node.new(n=>40);
$tree.append(30, 50, 25, 35, 45, 60, 15, 28, 55, 70);

say $tree.pre-order;
say $tree.in-order;
say $tree.post-order;
