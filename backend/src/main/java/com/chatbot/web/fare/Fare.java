package com.chatbot.web.fare;

import lombok.Getter;
import lombok.Setter;
import lombok.ToString;
import org.springframework.stereotype.Component;

@Getter
@Setter
@ToString
@Component
public class Fare {
    public int fareId;
    public String
            startName,
            arriveName,
            typeOne,
            typeTwo,
            typeThree,
            typeFour,
            typeFive,
            typeLightCar;
}
