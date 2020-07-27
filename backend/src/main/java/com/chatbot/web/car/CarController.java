package com.chatbot.web.car;

import com.chatbot.web.mappers.CarMapper;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@CrossOrigin(origins = "*",allowedHeaders = "*")
@RestController
@RequestMapping("/car")
public class CarController {

    @Autowired
    CarMapper carMapper;

    @GetMapping("/carSearch/{carName}")
    public Car[] select(@PathVariable String carName){
        String car = "%"+carName+"%";
        System.out.println(car);
        return carMapper.selectOne(car);
    }
    @GetMapping("/carAll")
    public List<Car> searchAll(){
        return carMapper.selectAll();
    }
}
