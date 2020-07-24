package com.chatbot.web.car;

import com.chatbot.web.mappers.CarMapper;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@CrossOrigin(origins = "*",allowedHeaders = "*")
@RestController
@RequestMapping("/car")
public class CarController {

    @Autowired
    CarMapper carMapper;

    @GetMapping("/carSearch")
    public Car[] select(String carName){
        carName = "%"+"모닝"+"%";
        return carMapper.selectOne(carName);
    }
}
