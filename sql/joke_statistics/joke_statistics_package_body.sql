/*
create or replace package joke_statistics_pkg
    is
    function get_average_review_score
        (
           joke in number
        )
        return number;
    function get_count_reviews
        (
           joke in number
        )
        return number;
    procedure get_all_statistics
        (
           joke in number,
            review_average out number,
            review_count out number
        );

end;
*/

--this package will save time as the database scales.  
--althought we can called .count / .avg functions from Django, it's much more efficient if we create package
create or replace package body joke_statistics_pkg
    is
    function get_average_review_score
        (
           joke in number
        )
        return number is
        avg_score number(10,2);
        begin
            select 
                avg(score)
                into avg_score
            from HUMOROUSLY_REVIEW
            where joke_id = joke;
            return avg_score;
        end;
    function get_count_reviews
        (
           joke in number
        )
        return number is
        review_count number(10);
        begin
            select
                count(*)
                into review_count
            from HUMOROUSLY_REVIEW
            where joke_id = joke;
            return review_count;
        end;
    procedure get_all_statistics
        (
           joke in number,
            review_average out number,
            review_count out number
        )
        is
        begin
            select 
                avg(score) avg_score,
                count(id) cnt_id
            into 
                review_average,
                review_count
            from HUMOROUSLY_REVIEW
            where joke_id = joke;
            
        end;
end;