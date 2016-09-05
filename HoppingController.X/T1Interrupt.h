/* 
 * File:   T1Interrupt.h
 * Author: JRK
 *
 * Created on June 29, 2014, 8:47 PM
 */

#ifndef T1INTERRUPT_H
#define	T1INTERRUPT_H

#include <xc.h>
#include "EncoderSetup.h"
#include "PWMSetup.h"
#include "UARTSetup.h"

#define INPUT_BUFFER_SIZE 11
#define OUTPUT_BUFFER_SIZE INPUT_BUFFER_SIZE+1

extern uint32_t time;

void __attribute__((__interrupt__, no_auto_psv)) _T1Interrupt(void);

#endif	/* T1INTERRUPT_H */

