class Notebook {
    has %!notes;
    has %!tags;

    method AT-KEY (Str $title) {
        %!notes{$title}
    }

    multi method ASSIGN-KEY (Str $title, Str $txt) {
        %!notes{$title} = $txt;
    }

    multi method ASSIGN-KEY (Str $title, (Str $txt, *@tags)) {
        %!notes{$title} = $txt;
        for @tags -> $tag { %!tags{$tag}.push($title); }
    }

    method search (*@tags) {
        @tags.map({@(%!tags{$_}) if %!tags{$_}}).flat.unique
    }
}

my $notebook = Notebook.new();
$notebook<list> = 'tomato, cheese, shoe', 'shopping', 'dinner';
$notebook<wist> = 'cards';
$notebook<gist> = 'github', 'coding', 'dinner';
say $notebook.search('shopping', 'dinner', 'blah');
