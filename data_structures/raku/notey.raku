class Notebook {
    has %!notes;
    has %!tags;

    method AT-KEY(Str $title) {
        say $title;
        %!notes{$title}
    }

    multi method ASSIGN-KEY(Str $title, Str $txt) {
        %!notes{$title} = $txt;
    }

    multi method ASSIGN-KEY(Str $title, (Str $txt, *@tags)) {
        %!notes{$title} = $txt;
        for @tags -> $tag { %!tags{$tag}.append($title); }
    }

    method search( *@tags ) {
        (map { @(%!tags{$_}) if %!tags{$_} }, @tags).flat.unique
    }

}

my $notebook = Notebook.new();
$notebook<list> = 'tomato, cheese, shoe', 'shopping', 'dinner';
$notebook<gist> = 'github', 'coding', 'dinner';
say $notebook.search('shopping', 'dinner', 'blah');
