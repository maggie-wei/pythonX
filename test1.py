#!/usr/bin/perl

# define Accumulate
package Accumulate ;

sub accumulate {

    my $listref = shift;    
    my $operation = shift;
    my $answers = [];
    
    for my $i (@$listref) {
        push @$answers, $operation->($i);
    }
    return $answers;
    
}

1;

