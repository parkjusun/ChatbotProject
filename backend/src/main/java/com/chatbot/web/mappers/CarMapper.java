package com.chatbot.web.mappers;

import com.chatbot.web.car.Car;
import org.springframework.stereotype.Repository;

import java.util.List;

@Repository
public interface CarMapper {
    public Car[] selectOne(String carName);
    public List<Car> selectAll();
}
