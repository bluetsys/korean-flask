package com.example.demo;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class TestController {
    
    @GetMapping(value = "/")
    public String testApi(){
        return "Hello World";
    }

	@GetMapping(value = "/health")
    public String healthApi(){
        return "Hello World";
    }
}