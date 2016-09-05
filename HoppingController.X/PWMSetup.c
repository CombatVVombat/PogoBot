#include "PWMSetup.h"

void PWMSetup()
{
    // Auxiliary Clock Setup

    // PTCON
    PTCONbits.PTEN = 0;     // Disable PWM before changing PTCON values
    PTCONbits.PTSIDL = 0;   // PWM timebase runs in CPU idle
    PTCONbits.SESTAT = 0;   // Shrug
    PTCONbits.SEIEN = 0;    // Special Event Interrupt Disabled
    PTCONbits.EIPU = 0;     // Only update on cycle boundaries
    PTCONbits.SYNCPOL = 0;  // Sync Input/Output polarity Normal
    PTCONbits.SYNCOEN = 0;  // Primary Time Base Sync Enable bit
    PTCONbits.SYNCEN = 0;   // External Time base sync
    PTCONbits.SYNCSRC = 0;  // Sync1 input from PPS
    PTCONbits.SEVTPS = 0;   // 1:1 Postscalar Special Event Trigger
    
    // PTCON2
    PTCON2bits.PCLKDIV = 0; // Divide timebase by 1

    // CHOP
    CHOPbits.CHPCLKEN = 0;  // Chop Clock Disabled

    // PWMCON1
    PWMCON1bits.FLTSTAT = 0;    // Fault Status Flag
    PWMCON1bits.CLSTAT = 0;     // Current Limit Interrupt Flag
    PWMCON1bits.TRGSTAT = 0;    // Trigger Interrupt Flag
    PWMCON1bits.FLTIEN = 0;     // Fault Interrupt Enable/Disable
    PWMCON1bits.CLIEN = 0;      // Current-Limit Interrupt Enable/Disable
    PWMCON1bits.TRGIEN = 0;     // Trigger Event Interrupts Enable/Disable
    PWMCON1bits.ITB = 0;        // Period by PTPER register
    PWMCON1bits.MDCS = 1;       // Use MDC as duty cycle register
    PWMCON1bits.DTC = 2;        // Dead Time Disabled
    PWMCON1bits.DTCP = 0;       // Dead Time Settings
    PWMCON1bits.MTBS = 0;       // Use Primary Master Time Base
    PWMCON1bits.CAM = 0;        // Edge Aligned
    PWMCON1bits.XPRES = 0;      // External pins do not effect PWM time base
    PWMCON1bits.IUE = 0;        // Updates on PWM period boundary

    // IOCON1
    IOCON1bits.PENH = 0;        // PWM1-High Pin general I/O
    IOCON1bits.PENL = 1;        // PWM1-Low Pin is controlled by PWM
    IOCON1bits.POLH = 0;        // Active-High
    IOCON1bits.POLL = 0;        // Active-High
    IOCON1bits.PMOD = 1;        // Redundant Mode
    IOCON1bits.OVRENH = 0;      // PWM Generator Controls High Pin
    IOCON1bits.OVRENL = 0;      // PWM Generator Controls Low Pin
    IOCON1bits.FLTDAT = 0;      // Drive pins to this state if FAULT
    IOCON1bits.CLDAT = 0;       // Drive pins to this state is Current-Limit Fault
    IOCON1bits.SWAP = 0;        // Flip low and high PWM pins?
    IOCON1bits.OSYNC = 0;       // Output overrides occur on next CPU Clock Boundary

    // IOCON2
    IOCON2bits.PENH = 0;        // Controlled by GPIO
    IOCON2bits.PENL = 0;        // Controlled by GPIO
    
    // IOCON3
    IOCON3bits.PENH = 0;        // Controlled by GPIO
    IOCON3bits.PENL = 0;        // Controlled by GPIO

    // FCLCON1
    FCLCON1bits.CLSRC = 0;      // Current-Limit Control Signal Source Select
    FCLCON1bits.CLPOL = 0;      // Current-Limit Polarity
    FCLCON1bits.CLMOD = 0;      // Current-Limit Enable/Disable
    FCLCON1bits.FLTSRC = 0;     // Fault Control Signal Source Select
    FCLCON1bits.FLTPOL = 0;     // Fault Control Polarity
    FCLCON1bits.FLTMOD = 3;     // Fault Input Disabled

    // AUXCON
    AUXCON1bits.BLANKSEL = 0;   // State Blanking (Whatever that is?)
    AUXCON1bits.CHOPSEL = 0;    // Chop CLock Select
    AUXCON1bits.CHOPHEN = 0;    // Chopping on High Pin Enable/Disable
    AUXCON1bits.CHOPLEN = 0;    // Chopping on Low Pin Enable/Disable

    // Set Period & Starting Duty Cycle
    PTPER = PWM_PERIOD;     // PWM Period
    MDC = 0;                // Initial Duty Cycle
}

void EnablePWM()
{
    PTCONbits.PTEN = 1;
}

void DisablePWM()
{
    PTCONbits.PTEN = 0;
}

void SetPowerOpenLoop(signed char Percent)
{
    if(Percent>0)
    {
        MOTOR_CTRL_A = 1;
        MOTOR_CTRL_B = 0;
    }
    else
    {
        MOTOR_CTRL_A = 0;
        MOTOR_CTRL_B = 1;
        Percent *= -1;
    }
    if(Percent > 100)
        Percent = 100;
    if(Percent < -100)
        Percent = -100;
    
    MDC = (unsigned int)((PWM_PERIOD * (unsigned long)Percent) / 100);
}