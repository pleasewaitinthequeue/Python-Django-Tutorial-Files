create or replace trigger humorously_review_insert_listener
    after insert on humorously_review
    for each row
    
    begin
        insert into journal (
            entity_id,
            entity_name,
            entity_desc,
            created,
            entity_type
        )         
        values (
                --"ID" number(11,0)
            :new.id, --"ENTITY_ID" number(11,0),
            :new.title, --"ENTITY_NAME" nvarchar2(200),
            :new.text, --"ENTITY_DESC" nvarchar2(200),
            current_timestamp, --"CREATED" timestamp (6) not null enable,
            'Review' --primary key ("ID")
        );
    end; 