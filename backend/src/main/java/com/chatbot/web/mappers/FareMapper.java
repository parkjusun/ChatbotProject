package com.chatbot.web.mappers;


import com.chatbot.web.fare.Fare;
import org.springframework.stereotype.Repository;

import java.util.List;

@Repository
public interface FareMapper {
    public List<Fare> selectOne(String startName,String arriveName);
    public List<Fare> selectAll();
}
