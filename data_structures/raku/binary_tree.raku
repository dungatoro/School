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

    method pre-order{flat($!n,$!l.defined??$!l.pre-order!!(),$!r.defined??$!r.pre-order!!())}
    method in-order{flat($!l.defined??$!l.in-order!!(),$!n,$!r.defined??$!r.in-order!!())}
    method post-order{flat($!l.defined??$!l.post-order!!(),$!r.defined??$!r.post-order!!(),$!n)}

    method rows ($depth=0, @rows=[]) {
        @rows.push([]) if @rows.elems <= $depth;
        @rows[$depth].push($!n);
        for $!l, $!r -> $node {
            if $node.defined {
                $node.rows($depth+1, @rows);
            } else {
                @rows.push([]) if @rows.elems <= $depth+1;
                @rows[$depth+1].push(Nil);
            }
        }
        @rows
    }

    method display {
        my @rows-strs = self.rows.map({[$^a.map({$^b.defined??$^b!!'  '}).join(' ')]});
        # my @rows-strs = @rows.map({$^a.map({say $^b}).join(' ')});
        say $_ for @rows-strs;
    }

    # def display(self):
	# 	rows = self.rows()
	# 	rows_strs = [[str(i) if i!=None else '  ' for i in r] for r in rows]
	# 	branches =  ['']+[['  ' if i==None else (' /' if n%2==0 else '\\ ') for n, i in enumerate(r)] for r in rows[1:]]

	# 	for i, (row, branch) in enumerate(zip(rows_strs, branches)): 
	# 		space = ' '*((len(rows)-i)**2)
	# 		print(space+space.join(branch))
	# 		print(space+space.join(row))
}

my $tree = Node.new(n=>40);
$tree.append(30, 50, 25, 35, 45, 60, 15, 28, 55, 70);

$tree.display;
