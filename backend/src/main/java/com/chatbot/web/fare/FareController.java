package com.chatbot.web.fare;


import com.chatbot.web.mappers.FareMapper;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@CrossOrigin(origins = "*",allowedHeaders = "*")
@RestController
@RequestMapping("/fare")
public class FareController {
    @Autowired
    FareMapper fareMapper;

    @GetMapping("/search/{startName}/{arriveName}")
    public List<Fare> Search(@PathVariable String startName,
                             @PathVariable String arriveName ){
        System.out.println("시작도시:"+startName+"도착도시:"+arriveName+"결과"+fareMapper.selectOne(startName,arriveName));
        return fareMapper.selectOne(startName,arriveName);
    }

    @GetMapping("/all")
    public List<Fare> All(){
        System.out.println(fareMapper.selectAll());
        return fareMapper.selectAll();
    }
}
