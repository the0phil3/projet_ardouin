<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
    xmlns:xs="http://www.w3.org/2001/XMLSchema"
    exclude-result-prefixes="xs"
    version="2.0">
    
    <xsl:output encoding="UTF-8" method="xml" omit-xml-declaration="no" indent="yes"/>
    
    <xsl:template match="/">
        <xsl:result-document href="/Users/Theo/dev/projet_ardouin/sqlite2xml/output/tome1_sortie.xml" method="xml">
            <xsl:element name="dsc">

                <xsl:apply-templates select="xml:xml"/>

            </xsl:element>   
        </xsl:result-document>
    </xsl:template>
    
    <xsl:template match="//DATA_RECORD">
        <xsl:element name="DATA_RECORD">
            <xsl:element name="level">item</xsl:element>
            <xsl:element name="id">test</xsl:element>
        </xsl:element>
        <xsl:apply-templates/>
    </xsl:template>
    
</xsl:stylesheet>