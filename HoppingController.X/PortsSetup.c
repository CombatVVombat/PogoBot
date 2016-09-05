#include "PortsSetup.h"

void PortsSetup()
{
    //// ADC For Current Sense ////
    AD1CON1bits.ADON = 0;
    AD1CON1bits.AD12B = 1;              // 12bit ADC
    AD1CON3bits.ADRC = 0;               // Use system clock
    AD1CON3bits.ADCS = 0b11111111;      // x 256
    AD1CON1bits.ASAM = 1;               // Sampling begins when last conversion completes
    AD1CON1bits.SSRCG = 0;
    AD1CON1bits.SSRC = 0b00000000;      // Manual Conversion Start
    AD1CON2bits.VCFG = 0;               // VDD/VSS references
    AD1CON3bits.ADCS = 0;               // TBD
    AD1CHS0bits.CH0SB = 1;              // AN1 -> Channel 0
    ANSELAbits.ANSA1 = 1;               // AN1 as analog
    TRISAbits.TRISA1 = 1;               // AN1 Input Direction
    AD1CON1bits.ADON = 1;               // ADC for Current Sense On
    
    //// Motor Control ////
    TRISBbits.TRISB15 = 0;      // Output for PWM
    TRISBbits.TRISB10 = 0;      // Output IN-B to motor driver
    TRISBbits.TRISB11 = 0;      // Output IN_A to motor driver

    //// Encoder ////
    TRISBbits.TRISB12 = 1;      // Input for encoder X
    TRISBbits.TRISB13 = 1;      // Input for encoder B
    TRISBbits.TRISB14 = 1;      // Input for encoder A
    CNPDBbits.CNPDB12 = 1;      // Internal Pull-Down
    CNPDBbits.CNPDB13 = 1;      // Internal Pull-Down
    CNPDBbits.CNPDB14 = 1;      // Internal Pull-Down

    //// Disable CTMU on B13 ////
    CTMUCON1bits.CTMUEN = 0;

    //// Serial ////
    TRISBbits.TRISB3 = 0;       // TX Pin
    TRISBbits.TRISB2 = 1;       // RX Pin
    ANSELBbits.ANSB2 = 0;
    ANSELBbits.ANSB3 = 0;
    CM1CONbits.CON = 0;         // Disable Comparitor on these pins
    CNPDBbits.CNPDB2 = 1;       // Internal Pull-Down
    
    PPSUnLock;
    PPSInput(IN_FN_PPS_U1RX, IN_PIN_PPS_RPI34);      // UART1 from Rs232->Pic (RX)
    PPSOutput(OUT_FN_PPS_U1TX, OUT_PIN_PPS_RP35);    // UART1 from Pic->Rs232 (TX)

    PPSInput(IN_FN_PPS_QEA1, IN_PIN_PPS_RPI46);      // QEI1 A
    PPSInput(IN_FN_PPS_QEB1, IN_PIN_PPS_RPI45);      // QEI1 B
    PPSInput(IN_FN_PPS_QEI1, IN_PIN_PPS_RPI44);      // QEI1 Index
    PPSLock;
}
