package com.chatbot.web.mappers;

import com.chatbot.web.user.User;
import org.springframework.stereotype.Repository;

@Repository
public interface UserMapper {
    public User insertUser(User user);
    public User login(User user);

}
