begin
    dbms_output.put_line(joke_statistics_pkg.get_average_review_score(1));
    dbms_output.put_line(joke_statistics_pkg.get_count_reviews(1));
end;