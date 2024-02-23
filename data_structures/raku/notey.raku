class Notebook {
    has %!notes;
    has %!tags;

    method AT-KEY($title) {
        say $title;
        %!notes{$title}
    }

    method ASSIGN-KEY($title, ($txt, *@tags)) {
        %!notes{$title} = $txt;
        for @tags -> $tag { %!tags{$tag}.append($title); }
    }

    method search( *@tags ) {
        map { %!tags{$_} if %!tags{$_} }, @tags
    }

}

my $notebook = Notebook.new();
$notebook<list> = 'tomato, cheese, shoe', 'shopping', 'dinner';
$notebook<gist> = 'github', 'coding', 'dinner';
say $notebook.search('shopping', 'dinner', 'blah');
