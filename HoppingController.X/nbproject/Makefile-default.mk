#
# Generated Makefile - do not edit!
#
# Edit the Makefile in the project folder instead (../Makefile). Each target
# has a -pre and a -post target defined where you can add customized code.
#
# This makefile implements configuration specific macros and targets.


# Include project Makefile
ifeq "${IGNORE_LOCAL}" "TRUE"
# do not include local makefile. User is passing all local related variables already
else
include Makefile
# Include makefile containing local settings
ifeq "$(wildcard nbproject/Makefile-local-default.mk)" "nbproject/Makefile-local-default.mk"
include nbproject/Makefile-local-default.mk
endif
endif

# Environment
MKDIR=gnumkdir -p
RM=rm -f 
MV=mv 
CP=cp 

# Macros
CND_CONF=default
ifeq ($(TYPE_IMAGE), DEBUG_RUN)
IMAGE_TYPE=debug
OUTPUT_SUFFIX=elf
DEBUGGABLE_SUFFIX=elf
FINAL_IMAGE=dist/${CND_CONF}/${IMAGE_TYPE}/HoppingController.X.${IMAGE_TYPE}.${OUTPUT_SUFFIX}
else
IMAGE_TYPE=production
OUTPUT_SUFFIX=hex
DEBUGGABLE_SUFFIX=elf
FINAL_IMAGE=dist/${CND_CONF}/${IMAGE_TYPE}/HoppingController.X.${IMAGE_TYPE}.${OUTPUT_SUFFIX}
endif

# Object Directory
OBJECTDIR=build/${CND_CONF}/${IMAGE_TYPE}

# Distribution Directory
DISTDIR=dist/${CND_CONF}/${IMAGE_TYPE}

# Source Files Quoted if spaced
SOURCEFILES_QUOTED_IF_SPACED=Main.c D:/Programming/LocalGit/PogoBot/HoppingController.X/InterruptSetup.c D:/Programming/LocalGit/PogoBot/HoppingController.X/OscSetup.c D:/Programming/LocalGit/PogoBot/HoppingController.X/PortsSetup.c D:/Programming/LocalGit/PogoBot/HoppingController.X/T1Interrupt.c D:/Programming/LocalGit/PogoBot/HoppingController.X/PWMSetup.c D:/Programming/LocalGit/PogoBot/HoppingController.X/EncoderSetup.c D:/Programming/LocalGit/PogoBot/HoppingController.X/UARTSetup.c

# Object Files Quoted if spaced
OBJECTFILES_QUOTED_IF_SPACED=${OBJECTDIR}/Main.o ${OBJECTDIR}/_ext/4861995/InterruptSetup.o ${OBJECTDIR}/_ext/4861995/OscSetup.o ${OBJECTDIR}/_ext/4861995/PortsSetup.o ${OBJECTDIR}/_ext/4861995/T1Interrupt.o ${OBJECTDIR}/_ext/4861995/PWMSetup.o ${OBJECTDIR}/_ext/4861995/EncoderSetup.o ${OBJECTDIR}/_ext/4861995/UARTSetup.o
POSSIBLE_DEPFILES=${OBJECTDIR}/Main.o.d ${OBJECTDIR}/_ext/4861995/InterruptSetup.o.d ${OBJECTDIR}/_ext/4861995/OscSetup.o.d ${OBJECTDIR}/_ext/4861995/PortsSetup.o.d ${OBJECTDIR}/_ext/4861995/T1Interrupt.o.d ${OBJECTDIR}/_ext/4861995/PWMSetup.o.d ${OBJECTDIR}/_ext/4861995/EncoderSetup.o.d ${OBJECTDIR}/_ext/4861995/UARTSetup.o.d

# Object Files
OBJECTFILES=${OBJECTDIR}/Main.o ${OBJECTDIR}/_ext/4861995/InterruptSetup.o ${OBJECTDIR}/_ext/4861995/OscSetup.o ${OBJECTDIR}/_ext/4861995/PortsSetup.o ${OBJECTDIR}/_ext/4861995/T1Interrupt.o ${OBJECTDIR}/_ext/4861995/PWMSetup.o ${OBJECTDIR}/_ext/4861995/EncoderSetup.o ${OBJECTDIR}/_ext/4861995/UARTSetup.o

# Source Files
SOURCEFILES=Main.c D:/Programming/LocalGit/PogoBot/HoppingController.X/InterruptSetup.c D:/Programming/LocalGit/PogoBot/HoppingController.X/OscSetup.c D:/Programming/LocalGit/PogoBot/HoppingController.X/PortsSetup.c D:/Programming/LocalGit/PogoBot/HoppingController.X/T1Interrupt.c D:/Programming/LocalGit/PogoBot/HoppingController.X/PWMSetup.c D:/Programming/LocalGit/PogoBot/HoppingController.X/EncoderSetup.c D:/Programming/LocalGit/PogoBot/HoppingController.X/UARTSetup.c


CFLAGS=
ASFLAGS=
LDLIBSOPTIONS=

############# Tool locations ##########################################
# If you copy a project from one host to another, the path where the  #
# compiler is installed may be different.                             #
# If you open this project with MPLAB X in the new host, this         #
# makefile will be regenerated and the paths will be corrected.       #
#######################################################################
# fixDeps replaces a bunch of sed/cat/printf statements that slow down the build
FIXDEPS=fixDeps

.build-conf:  ${BUILD_SUBPROJECTS}
	${MAKE} ${MAKE_OPTIONS} -f nbproject/Makefile-default.mk dist/${CND_CONF}/${IMAGE_TYPE}/HoppingController.X.${IMAGE_TYPE}.${OUTPUT_SUFFIX}

MP_PROCESSOR_OPTION=33EP256MC202
MP_LINKER_FILE_OPTION=,--script=p33EP256MC202.gld
# ------------------------------------------------------------------------------------
# Rules for buildStep: compile
ifeq ($(TYPE_IMAGE), DEBUG_RUN)
${OBJECTDIR}/Main.o: Main.c  nbproject/Makefile-${CND_CONF}.mk
	@${MKDIR} ${OBJECTDIR} 
	@${RM} ${OBJECTDIR}/Main.o.d 
	@${RM} ${OBJECTDIR}/Main.o 
	${MP_CC} $(MP_EXTRA_CC_PRE)  Main.c  -o ${OBJECTDIR}/Main.o  -c -mcpu=$(MP_PROCESSOR_OPTION)  -MMD -MF "${OBJECTDIR}/Main.o.d"      -g -D__DEBUG -D__MPLAB_DEBUGGER_PK3=1  -mno-eds-warn  -omf=elf -O0 -msmart-io=1 -Wall -msfr-warn=off -std=gnu99
	@${FIXDEPS} "${OBJECTDIR}/Main.o.d" $(SILENT)  -rsi ${MP_CC_DIR}../ 
	
${OBJECTDIR}/_ext/4861995/InterruptSetup.o: D:/Programming/LocalGit/PogoBot/HoppingController.X/InterruptSetup.c  nbproject/Makefile-${CND_CONF}.mk
	@${MKDIR} ${OBJECTDIR}/_ext/4861995 
	@${RM} ${OBJECTDIR}/_ext/4861995/InterruptSetup.o.d 
	@${RM} ${OBJECTDIR}/_ext/4861995/InterruptSetup.o 
	${MP_CC} $(MP_EXTRA_CC_PRE)  D:/Programming/LocalGit/PogoBot/HoppingController.X/InterruptSetup.c  -o ${OBJECTDIR}/_ext/4861995/InterruptSetup.o  -c -mcpu=$(MP_PROCESSOR_OPTION)  -MMD -MF "${OBJECTDIR}/_ext/4861995/InterruptSetup.o.d"      -g -D__DEBUG -D__MPLAB_DEBUGGER_PK3=1  -mno-eds-warn  -omf=elf -O0 -msmart-io=1 -Wall -msfr-warn=off -std=gnu99
	@${FIXDEPS} "${OBJECTDIR}/_ext/4861995/InterruptSetup.o.d" $(SILENT)  -rsi ${MP_CC_DIR}../ 
	
${OBJECTDIR}/_ext/4861995/OscSetup.o: D:/Programming/LocalGit/PogoBot/HoppingController.X/OscSetup.c  nbproject/Makefile-${CND_CONF}.mk
	@${MKDIR} ${OBJECTDIR}/_ext/4861995 
	@${RM} ${OBJECTDIR}/_ext/4861995/OscSetup.o.d 
	@${RM} ${OBJECTDIR}/_ext/4861995/OscSetup.o 
	${MP_CC} $(MP_EXTRA_CC_PRE)  D:/Programming/LocalGit/PogoBot/HoppingController.X/OscSetup.c  -o ${OBJECTDIR}/_ext/4861995/OscSetup.o  -c -mcpu=$(MP_PROCESSOR_OPTION)  -MMD -MF "${OBJECTDIR}/_ext/4861995/OscSetup.o.d"      -g -D__DEBUG -D__MPLAB_DEBUGGER_PK3=1  -mno-eds-warn  -omf=elf -O0 -msmart-io=1 -Wall -msfr-warn=off -std=gnu99
	@${FIXDEPS} "${OBJECTDIR}/_ext/4861995/OscSetup.o.d" $(SILENT)  -rsi ${MP_CC_DIR}../ 
	
${OBJECTDIR}/_ext/4861995/PortsSetup.o: D:/Programming/LocalGit/PogoBot/HoppingController.X/PortsSetup.c  nbproject/Makefile-${CND_CONF}.mk
	@${MKDIR} ${OBJECTDIR}/_ext/4861995 
	@${RM} ${OBJECTDIR}/_ext/4861995/PortsSetup.o.d 
	@${RM} ${OBJECTDIR}/_ext/4861995/PortsSetup.o 
	${MP_CC} $(MP_EXTRA_CC_PRE)  D:/Programming/LocalGit/PogoBot/HoppingController.X/PortsSetup.c  -o ${OBJECTDIR}/_ext/4861995/PortsSetup.o  -c -mcpu=$(MP_PROCESSOR_OPTION)  -MMD -MF "${OBJECTDIR}/_ext/4861995/PortsSetup.o.d"      -g -D__DEBUG -D__MPLAB_DEBUGGER_PK3=1  -mno-eds-warn  -omf=elf -O0 -msmart-io=1 -Wall -msfr-warn=off -std=gnu99
	@${FIXDEPS} "${OBJECTDIR}/_ext/4861995/PortsSetup.o.d" $(SILENT)  -rsi ${MP_CC_DIR}../ 
	
${OBJECTDIR}/_ext/4861995/T1Interrupt.o: D:/Programming/LocalGit/PogoBot/HoppingController.X/T1Interrupt.c  nbproject/Makefile-${CND_CONF}.mk
	@${MKDIR} ${OBJECTDIR}/_ext/4861995 
	@${RM} ${OBJECTDIR}/_ext/4861995/T1Interrupt.o.d 
	@${RM} ${OBJECTDIR}/_ext/4861995/T1Interrupt.o 
	${MP_CC} $(MP_EXTRA_CC_PRE)  D:/Programming/LocalGit/PogoBot/HoppingController.X/T1Interrupt.c  -o ${OBJECTDIR}/_ext/4861995/T1Interrupt.o  -c -mcpu=$(MP_PROCESSOR_OPTION)  -MMD -MF "${OBJECTDIR}/_ext/4861995/T1Interrupt.o.d"      -g -D__DEBUG -D__MPLAB_DEBUGGER_PK3=1  -mno-eds-warn  -omf=elf -O0 -msmart-io=1 -Wall -msfr-warn=off -std=gnu99
	@${FIXDEPS} "${OBJECTDIR}/_ext/4861995/T1Interrupt.o.d" $(SILENT)  -rsi ${MP_CC_DIR}../ 
	
${OBJECTDIR}/_ext/4861995/PWMSetup.o: D:/Programming/LocalGit/PogoBot/HoppingController.X/PWMSetup.c  nbproject/Makefile-${CND_CONF}.mk
	@${MKDIR} ${OBJECTDIR}/_ext/4861995 
	@${RM} ${OBJECTDIR}/_ext/4861995/PWMSetup.o.d 
	@${RM} ${OBJECTDIR}/_ext/4861995/PWMSetup.o 
	${MP_CC} $(MP_EXTRA_CC_PRE)  D:/Programming/LocalGit/PogoBot/HoppingController.X/PWMSetup.c  -o ${OBJECTDIR}/_ext/4861995/PWMSetup.o  -c -mcpu=$(MP_PROCESSOR_OPTION)  -MMD -MF "${OBJECTDIR}/_ext/4861995/PWMSetup.o.d"      -g -D__DEBUG -D__MPLAB_DEBUGGER_PK3=1  -mno-eds-warn  -omf=elf -O0 -msmart-io=1 -Wall -msfr-warn=off -std=gnu99
	@${FIXDEPS} "${OBJECTDIR}/_ext/4861995/PWMSetup.o.d" $(SILENT)  -rsi ${MP_CC_DIR}../ 
	
${OBJECTDIR}/_ext/4861995/EncoderSetup.o: D:/Programming/LocalGit/PogoBot/HoppingController.X/EncoderSetup.c  nbproject/Makefile-${CND_CONF}.mk
	@${MKDIR} ${OBJECTDIR}/_ext/4861995 
	@${RM} ${OBJECTDIR}/_ext/4861995/EncoderSetup.o.d 
	@${RM} ${OBJECTDIR}/_ext/4861995/EncoderSetup.o 
	${MP_CC} $(MP_EXTRA_CC_PRE)  D:/Programming/LocalGit/PogoBot/HoppingController.X/EncoderSetup.c  -o ${OBJECTDIR}/_ext/4861995/EncoderSetup.o  -c -mcpu=$(MP_PROCESSOR_OPTION)  -MMD -MF "${OBJECTDIR}/_ext/4861995/EncoderSetup.o.d"      -g -D__DEBUG -D__MPLAB_DEBUGGER_PK3=1  -mno-eds-warn  -omf=elf -O0 -msmart-io=1 -Wall -msfr-warn=off -std=gnu99
	@${FIXDEPS} "${OBJECTDIR}/_ext/4861995/EncoderSetup.o.d" $(SILENT)  -rsi ${MP_CC_DIR}../ 
	
${OBJECTDIR}/_ext/4861995/UARTSetup.o: D:/Programming/LocalGit/PogoBot/HoppingController.X/UARTSetup.c  nbproject/Makefile-${CND_CONF}.mk
	@${MKDIR} ${OBJECTDIR}/_ext/4861995 
	@${RM} ${OBJECTDIR}/_ext/4861995/UARTSetup.o.d 
	@${RM} ${OBJECTDIR}/_ext/4861995/UARTSetup.o 
	${MP_CC} $(MP_EXTRA_CC_PRE)  D:/Programming/LocalGit/PogoBot/HoppingController.X/UARTSetup.c  -o ${OBJECTDIR}/_ext/4861995/UARTSetup.o  -c -mcpu=$(MP_PROCESSOR_OPTION)  -MMD -MF "${OBJECTDIR}/_ext/4861995/UARTSetup.o.d"      -g -D__DEBUG -D__MPLAB_DEBUGGER_PK3=1  -mno-eds-warn  -omf=elf -O0 -msmart-io=1 -Wall -msfr-warn=off -std=gnu99
	@${FIXDEPS} "${OBJECTDIR}/_ext/4861995/UARTSetup.o.d" $(SILENT)  -rsi ${MP_CC_DIR}../ 
	
else
${OBJECTDIR}/Main.o: Main.c  nbproject/Makefile-${CND_CONF}.mk
	@${MKDIR} ${OBJECTDIR} 
	@${RM} ${OBJECTDIR}/Main.o.d 
	@${RM} ${OBJECTDIR}/Main.o 
	${MP_CC} $(MP_EXTRA_CC_PRE)  Main.c  -o ${OBJECTDIR}/Main.o  -c -mcpu=$(MP_PROCESSOR_OPTION)  -MMD -MF "${OBJECTDIR}/Main.o.d"      -mno-eds-warn  -g -omf=elf -O0 -msmart-io=1 -Wall -msfr-warn=off -std=gnu99
	@${FIXDEPS} "${OBJECTDIR}/Main.o.d" $(SILENT)  -rsi ${MP_CC_DIR}../ 
	
${OBJECTDIR}/_ext/4861995/InterruptSetup.o: D:/Programming/LocalGit/PogoBot/HoppingController.X/InterruptSetup.c  nbproject/Makefile-${CND_CONF}.mk
	@${MKDIR} ${OBJECTDIR}/_ext/4861995 
	@${RM} ${OBJECTDIR}/_ext/4861995/InterruptSetup.o.d 
	@${RM} ${OBJECTDIR}/_ext/4861995/InterruptSetup.o 
	${MP_CC} $(MP_EXTRA_CC_PRE)  D:/Programming/LocalGit/PogoBot/HoppingController.X/InterruptSetup.c  -o ${OBJECTDIR}/_ext/4861995/InterruptSetup.o  -c -mcpu=$(MP_PROCESSOR_OPTION)  -MMD -MF "${OBJECTDIR}/_ext/4861995/InterruptSetup.o.d"      -mno-eds-warn  -g -omf=elf -O0 -msmart-io=1 -Wall -msfr-warn=off -std=gnu99
	@${FIXDEPS} "${OBJECTDIR}/_ext/4861995/InterruptSetup.o.d" $(SILENT)  -rsi ${MP_CC_DIR}../ 
	
${OBJECTDIR}/_ext/4861995/OscSetup.o: D:/Programming/LocalGit/PogoBot/HoppingController.X/OscSetup.c  nbproject/Makefile-${CND_CONF}.mk
	@${MKDIR} ${OBJECTDIR}/_ext/4861995 
	@${RM} ${OBJECTDIR}/_ext/4861995/OscSetup.o.d 
	@${RM} ${OBJECTDIR}/_ext/4861995/OscSetup.o 
	${MP_CC} $(MP_EXTRA_CC_PRE)  D:/Programming/LocalGit/PogoBot/HoppingController.X/OscSetup.c  -o ${OBJECTDIR}/_ext/4861995/OscSetup.o  -c -mcpu=$(MP_PROCESSOR_OPTION)  -MMD -MF "${OBJECTDIR}/_ext/4861995/OscSetup.o.d"      -mno-eds-warn  -g -omf=elf -O0 -msmart-io=1 -Wall -msfr-warn=off -std=gnu99
	@${FIXDEPS} "${OBJECTDIR}/_ext/4861995/OscSetup.o.d" $(SILENT)  -rsi ${MP_CC_DIR}../ 
	
${OBJECTDIR}/_ext/4861995/PortsSetup.o: D:/Programming/LocalGit/PogoBot/HoppingController.X/PortsSetup.c  nbproject/Makefile-${CND_CONF}.mk
	@${MKDIR} ${OBJECTDIR}/_ext/4861995 
	@${RM} ${OBJECTDIR}/_ext/4861995/PortsSetup.o.d 
	@${RM} ${OBJECTDIR}/_ext/4861995/PortsSetup.o 
	${MP_CC} $(MP_EXTRA_CC_PRE)  D:/Programming/LocalGit/PogoBot/HoppingController.X/PortsSetup.c  -o ${OBJECTDIR}/_ext/4861995/PortsSetup.o  -c -mcpu=$(MP_PROCESSOR_OPTION)  -MMD -MF "${OBJECTDIR}/_ext/4861995/PortsSetup.o.d"      -mno-eds-warn  -g -omf=elf -O0 -msmart-io=1 -Wall -msfr-warn=off -std=gnu99
	@${FIXDEPS} "${OBJECTDIR}/_ext/4861995/PortsSetup.o.d" $(SILENT)  -rsi ${MP_CC_DIR}../ 
	
${OBJECTDIR}/_ext/4861995/T1Interrupt.o: D:/Programming/LocalGit/PogoBot/HoppingController.X/T1Interrupt.c  nbproject/Makefile-${CND_CONF}.mk
	@${MKDIR} ${OBJECTDIR}/_ext/4861995 
	@${RM} ${OBJECTDIR}/_ext/4861995/T1Interrupt.o.d 
	@${RM} ${OBJECTDIR}/_ext/4861995/T1Interrupt.o 
	${MP_CC} $(MP_EXTRA_CC_PRE)  D:/Programming/LocalGit/PogoBot/HoppingController.X/T1Interrupt.c  -o ${OBJECTDIR}/_ext/4861995/T1Interrupt.o  -c -mcpu=$(MP_PROCESSOR_OPTION)  -MMD -MF "${OBJECTDIR}/_ext/4861995/T1Interrupt.o.d"      -mno-eds-warn  -g -omf=elf -O0 -msmart-io=1 -Wall -msfr-warn=off -std=gnu99
	@${FIXDEPS} "${OBJECTDIR}/_ext/4861995/T1Interrupt.o.d" $(SILENT)  -rsi ${MP_CC_DIR}../ 
	
${OBJECTDIR}/_ext/4861995/PWMSetup.o: D:/Programming/LocalGit/PogoBot/HoppingController.X/PWMSetup.c  nbproject/Makefile-${CND_CONF}.mk
	@${MKDIR} ${OBJECTDIR}/_ext/4861995 
	@${RM} ${OBJECTDIR}/_ext/4861995/PWMSetup.o.d 
	@${RM} ${OBJECTDIR}/_ext/4861995/PWMSetup.o 
	${MP_CC} $(MP_EXTRA_CC_PRE)  D:/Programming/LocalGit/PogoBot/HoppingController.X/PWMSetup.c  -o ${OBJECTDIR}/_ext/4861995/PWMSetup.o  -c -mcpu=$(MP_PROCESSOR_OPTION)  -MMD -MF "${OBJECTDIR}/_ext/4861995/PWMSetup.o.d"      -mno-eds-warn  -g -omf=elf -O0 -msmart-io=1 -Wall -msfr-warn=off -std=gnu99
	@${FIXDEPS} "${OBJECTDIR}/_ext/4861995/PWMSetup.o.d" $(SILENT)  -rsi ${MP_CC_DIR}../ 
	
${OBJECTDIR}/_ext/4861995/EncoderSetup.o: D:/Programming/LocalGit/PogoBot/HoppingController.X/EncoderSetup.c  nbproject/Makefile-${CND_CONF}.mk
	@${MKDIR} ${OBJECTDIR}/_ext/4861995 
	@${RM} ${OBJECTDIR}/_ext/4861995/EncoderSetup.o.d 
	@${RM} ${OBJECTDIR}/_ext/4861995/EncoderSetup.o 
	${MP_CC} $(MP_EXTRA_CC_PRE)  D:/Programming/LocalGit/PogoBot/HoppingController.X/EncoderSetup.c  -o ${OBJECTDIR}/_ext/4861995/EncoderSetup.o  -c -mcpu=$(MP_PROCESSOR_OPTION)  -MMD -MF "${OBJECTDIR}/_ext/4861995/EncoderSetup.o.d"      -mno-eds-warn  -g -omf=elf -O0 -msmart-io=1 -Wall -msfr-warn=off -std=gnu99
	@${FIXDEPS} "${OBJECTDIR}/_ext/4861995/EncoderSetup.o.d" $(SILENT)  -rsi ${MP_CC_DIR}../ 
	
${OBJECTDIR}/_ext/4861995/UARTSetup.o: D:/Programming/LocalGit/PogoBot/HoppingController.X/UARTSetup.c  nbproject/Makefile-${CND_CONF}.mk
	@${MKDIR} ${OBJECTDIR}/_ext/4861995 
	@${RM} ${OBJECTDIR}/_ext/4861995/UARTSetup.o.d 
	@${RM} ${OBJECTDIR}/_ext/4861995/UARTSetup.o 
	${MP_CC} $(MP_EXTRA_CC_PRE)  D:/Programming/LocalGit/PogoBot/HoppingController.X/UARTSetup.c  -o ${OBJECTDIR}/_ext/4861995/UARTSetup.o  -c -mcpu=$(MP_PROCESSOR_OPTION)  -MMD -MF "${OBJECTDIR}/_ext/4861995/UARTSetup.o.d"      -mno-eds-warn  -g -omf=elf -O0 -msmart-io=1 -Wall -msfr-warn=off -std=gnu99
	@${FIXDEPS} "${OBJECTDIR}/_ext/4861995/UARTSetup.o.d" $(SILENT)  -rsi ${MP_CC_DIR}../ 
	
endif

# ------------------------------------------------------------------------------------
# Rules for buildStep: assemble
ifeq ($(TYPE_IMAGE), DEBUG_RUN)
else
endif

# ------------------------------------------------------------------------------------
# Rules for buildStep: assemblePreproc
ifeq ($(TYPE_IMAGE), DEBUG_RUN)
else
endif

# ------------------------------------------------------------------------------------
# Rules for buildStep: link
ifeq ($(TYPE_IMAGE), DEBUG_RUN)
dist/${CND_CONF}/${IMAGE_TYPE}/HoppingController.X.${IMAGE_TYPE}.${OUTPUT_SUFFIX}: ${OBJECTFILES}  nbproject/Makefile-${CND_CONF}.mk    
	@${MKDIR} dist/${CND_CONF}/${IMAGE_TYPE} 
	${MP_CC} $(MP_EXTRA_LD_PRE)  -o dist/${CND_CONF}/${IMAGE_TYPE}/HoppingController.X.${IMAGE_TYPE}.${OUTPUT_SUFFIX}  ${OBJECTFILES_QUOTED_IF_SPACED}      -mcpu=$(MP_PROCESSOR_OPTION)        -D__DEBUG -D__MPLAB_DEBUGGER_PK3=1  -omf=elf -Wl,--local-stack,--defsym=__MPLAB_BUILD=1,--defsym=__ICD2RAM=1,--defsym=__MPLAB_DEBUG=1,--defsym=__DEBUG=1,--defsym=__MPLAB_DEBUGGER_PK3=1,$(MP_LINKER_FILE_OPTION),--stack=16,--check-sections,--data-init,--pack-data,--handles,--isr,--no-gc-sections,--fill-upper=0,--stackguard=16,--no-force-link,--smart-io,-Map="${DISTDIR}/${PROJECTNAME}.${IMAGE_TYPE}.map",--report-mem$(MP_EXTRA_LD_POST) 
	
else
dist/${CND_CONF}/${IMAGE_TYPE}/HoppingController.X.${IMAGE_TYPE}.${OUTPUT_SUFFIX}: ${OBJECTFILES}  nbproject/Makefile-${CND_CONF}.mk   
	@${MKDIR} dist/${CND_CONF}/${IMAGE_TYPE} 
	${MP_CC} $(MP_EXTRA_LD_PRE)  -o dist/${CND_CONF}/${IMAGE_TYPE}/HoppingController.X.${IMAGE_TYPE}.${DEBUGGABLE_SUFFIX}  ${OBJECTFILES_QUOTED_IF_SPACED}      -mcpu=$(MP_PROCESSOR_OPTION)        -omf=elf -Wl,--local-stack,--defsym=__MPLAB_BUILD=1,$(MP_LINKER_FILE_OPTION),--stack=16,--check-sections,--data-init,--pack-data,--handles,--isr,--no-gc-sections,--fill-upper=0,--stackguard=16,--no-force-link,--smart-io,-Map="${DISTDIR}/${PROJECTNAME}.${IMAGE_TYPE}.map",--report-mem$(MP_EXTRA_LD_POST) 
	${MP_CC_DIR}\\xc16-bin2hex dist/${CND_CONF}/${IMAGE_TYPE}/HoppingController.X.${IMAGE_TYPE}.${DEBUGGABLE_SUFFIX} -a  -omf=elf 
	
endif


# Subprojects
.build-subprojects:


# Subprojects
.clean-subprojects:

# Clean Targets
.clean-conf: ${CLEAN_SUBPROJECTS}
	${RM} -r build/default
	${RM} -r dist/default

# Enable dependency checking
.dep.inc: .depcheck-impl

DEPFILES=$(shell mplabwildcard ${POSSIBLE_DEPFILES})
ifneq (${DEPFILES},)
include ${DEPFILES}
endif
