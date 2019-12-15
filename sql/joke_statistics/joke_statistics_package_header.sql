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