grant execute on utl_mail to system;
alter system set smtp_out_server = 'smtp.gmail.com:465' scope = both;
/*
  PROCEDURE send(sender         IN VARCHAR2 CHARACTER SET ANY_CS,
                 recipients     IN VARCHAR2 CHARACTER SET ANY_CS,
                 cc             IN VARCHAR2 CHARACTER SET ANY_CS DEFAULT NULL,
                 bcc            IN VARCHAR2 CHARACTER SET ANY_CS DEFAULT NULL,
                 subject        IN VARCHAR2 CHARACTER SET ANY_CS DEFAULT NULL,
                 message        IN VARCHAR2 CHARACTER SET ANY_CS DEFAULT NULL,
                 mime_type      IN VARCHAR2 CHARACTER SET ANY_CS 
                                   DEFAULT 'text/plain; charset=us-ascii',
                 priority       IN PLS_INTEGER DEFAULT 3,
                 replyto        IN VARCHAR2 CHARACTER SET ANY_CS DEFAULT NULL)
*/
begin
    utl_mail.send(
        sender => 'john.lairson@gmail.com',
        recipients => 'john.lairson@gmail.com',
        subject => 'Test Subject',
        message => 'Test Message'
    );
end;