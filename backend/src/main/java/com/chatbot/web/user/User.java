package com.chatbot.web.user;

import lombok.Getter;
import lombok.Setter;
import lombok.ToString;
import org.springframework.stereotype.Component;

@Getter
@Setter
@ToString
@Component
public class User {
    public String seq,userid, passwd,email, addr;
}
