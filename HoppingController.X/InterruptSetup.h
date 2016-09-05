/* 
 * File:   InterruptSetup.h
 * Author: JRK
 *
 * Created on April 23, 2013, 6:18 PM
 */

#ifndef INTERRUPTSETUP_H
#define	INTERRUPTSETUP_H

#include <xc.h>

void InterruptSetup();
void EnableT1Interrupt();
void DisableT1Interrupt();
void EnableT2Interrupt();
void DisableT2Interrupt();

#endif	/* INTERRUPTSETUP_H */

