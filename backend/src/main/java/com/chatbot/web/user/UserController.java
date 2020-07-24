package com.chatbot.web.user;


import com.chatbot.web.mappers.UserMapper;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

@CrossOrigin(origins = "*",allowedHeaders = "*")
@RestController
@RequestMapping("/user")
public class UserController {
    @Autowired
    UserMapper userMapper;


    @GetMapping("/join")
    public boolean join(){
        User newUser = new User();
        newUser.setUserid("v");
        newUser.setPasswd("v");
        newUser.setEmail("v");
        newUser.setAddr("v");
        System.out.println("들어온데이터:"+newUser.toString());
        return (userMapper.insertUser(newUser) == null)? true: false;
    }

    @GetMapping("/login")
    public boolean login(){
        User user = new User();
        user.setUserid("b");
        user.setPasswd("b");
        System.out.println("들어온데이터:"+user.toString());
        return (userMapper.login(user) != null)? true: false;
    }





}
