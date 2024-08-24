package org.sdet;

public class JavaSwitchCase {
    public static void main(String[] args){
        String city = "Kolkata";
        switch (city){
            case "Mumbai":
                System.out.println("Financial city");
                break;
            case "Kolkata":
                System.out.println("City of Joy");
                break;
            case "Delhi":
                System.out.println("Capital of the country");
                break;
            case "Banglore":
                System.out.println("Cyber city");
                break;
            default:
                System.out.println("May be Other Indian City");
                break;

        }

    }
}
