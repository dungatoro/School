class Notebook {
    has %!notes;
    has %!tags;

    method ASSIGN-KEY($title, ($txt, *@tags)) {
        %!notes{$title} = $txt;
        for @tags -> $tag { %!tags{$tag}.append($title); }
    }

    multi method search( *@tags ) {
        (map { %!tags{$_} if %!tags{$_} }, @tags).unique
    }

    multi method AT-KEY($title) {
        say $title;
        %!notes{$title}
    }
}

my $notebook = Notebook.new();
$notebook<list> = 'tomato, cheese, shoe', 'shopping', 'dinner';
say $notebook.search('shopping', 'dinner', 'blah');
