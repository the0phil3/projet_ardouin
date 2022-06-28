<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
    xmlns:xs="http://www.w3.org/2001/XMLSchema"
    exclude-result-prefixes="xs"
    version="2.0">
    
    <xsl:output encoding="UTF-8" method="xml" omit-xml-declaration="no" indent="yes"/>
    
    <xsl:template match="/">
        <xsl:result-document href="/Users/Theo/dev/projet_ardouin/sqlite2xml/output/tome1_sortie.xml" method="xml"/>
        <xsl:apply-templates/>
    </xsl:template>
    
    <xsl:variable name="entry" select="//DATA_RECORD[not(.=../../preceding-sibling::tome1)]"/>
    <xsl:variable name="folio" select="//DATA_RECORD[not(.=../../preceding-sibling::tome1)]/f1|f2|f3|f4|f5|f6|f7|f8|f9|f10|f11|f12|f13|f14|f15|f16|f17|f18|f19|f20|f21|f22|f23|f24|f25[not(.=../../preceding-sibling::DATA_RECORD)]"/> 
    
   <xsl:template match="/">
      <xsl:element name="desc">
          <xsl:for-each select="$entry">
              <xsl:element name="c">
                  <xsl:attribute name="level">item</xsl:attribute>
                  
                  <xsl:element name="did">
                      <xsl:element name="unitid">
                          <xsl:attribute name="type">cote</xsl:attribute>
                          <xsl:text>MR </xsl:text><xsl:apply-templates select="sserie"/><xsl:apply-templates select="serie"/>
                          <xsl:apply-templates select="ssserie"/><xsl:apply-templates select="atl"/><xsl:text> (Microfilm MR MI </xsl:text>
                          <xsl:apply-templates select="mf"/><xsl:text>), folio </xsl:text> 
                          <xsl:if test="f1 != ''">
                              <xsl:value-of select="f1"/>
                              <xsl:text>,</xsl:text>
                          </xsl:if>
                          <xsl:if test="f2 != ''">
                              <xsl:value-of select="f2"/>
                              <xsl:text>,</xsl:text>
                          </xsl:if>
                          <xsl:if test="f3 != ''">
                              <xsl:value-of select="f3"/>
                              <xsl:text>,</xsl:text>
                          </xsl:if>
                          <xsl:if test="f4 != ''">
                              <xsl:value-of select="f4"/>
                              <xsl:text>,</xsl:text>
                          </xsl:if>
                          <xsl:if test="f5 != ''">
                              <xsl:value-of select="f5"/>
                              <xsl:text>,</xsl:text>
                          </xsl:if>
                          <xsl:if test="f6 != ''">
                              <xsl:value-of select="f6"/>
                              <xsl:text>,</xsl:text>
                          </xsl:if>
                          <xsl:if test="f7 != ''">
                              <xsl:value-of select="f7"/>
                              <xsl:text>,</xsl:text>
                          </xsl:if>
                          <xsl:if test="f8 != ''">
                              <xsl:value-of select="f8"/>
                              <xsl:text>,</xsl:text>
                          </xsl:if>
                          <xsl:if test="f9 != ''">
                              <xsl:value-of select="f9"/>
                              <xsl:text>,</xsl:text>
                          </xsl:if>
                          <xsl:if test="f10 != ''">
                              <xsl:value-of select="f10"/>
                              <xsl:text>,</xsl:text>
                          </xsl:if>
                          <xsl:if test="f11 != ''">
                              <xsl:value-of select="f11"/>
                              <xsl:text>,</xsl:text>
                          </xsl:if>
                          <xsl:if test="f12 != ''">
                              <xsl:value-of select="f12"/>
                              <xsl:text>,</xsl:text>
                          </xsl:if>
                          <xsl:if test="f13 != ''">
                              <xsl:value-of select="f13"/>
                              <xsl:text>,</xsl:text>
                          </xsl:if>
                          <xsl:if test="f14 != ''">
                              <xsl:value-of select="f14"/>
                              <xsl:text>,</xsl:text>
                          </xsl:if>
                          <xsl:if test="f15 != ''">
                              <xsl:value-of select="f15"/>
                              <xsl:text>,</xsl:text>
                          </xsl:if>
                          <xsl:if test="f16 != ''">
                              <xsl:value-of select="f16"/>
                              <xsl:text>,</xsl:text>
                          </xsl:if>
                          <xsl:if test="f17 != ''">
                              <xsl:value-of select="f17"/>
                              <xsl:text>,</xsl:text>
                          </xsl:if>
                          <xsl:if test="f18 != ''">
                              <xsl:value-of select="f18"/>
                              <xsl:text>,</xsl:text>
                          </xsl:if>
                          <xsl:if test="f19 != ''">
                              <xsl:value-of select="f19"/>
                              <xsl:text>,</xsl:text>
                          </xsl:if>
                          <xsl:if test="f20 != ''">
                              <xsl:value-of select="f20"/>
                              <xsl:text>,</xsl:text>
                          </xsl:if>
                          <xsl:if test="f21 != ''">
                              <xsl:value-of select="f21"/>
                              <xsl:text>,</xsl:text>
                          </xsl:if>
                          <xsl:if test="f22 != ''">
                              <xsl:value-of select="f22"/>
                              <xsl:text>,</xsl:text>
                          </xsl:if>
                          <xsl:if test="f23 != ''">
                              <xsl:value-of select="f23"/>
                              <xsl:text>,</xsl:text>
                          </xsl:if>
                          <xsl:if test="f24 != ''">
                              <xsl:value-of select="f24"/>
                              <xsl:text>,</xsl:text>
                          </xsl:if>
                          <xsl:if test="f25 != ''">
                              <xsl:value-of select="f25"/>
                              <xsl:text>,</xsl:text>
                          </xsl:if>
                      </xsl:element>
                      <xsl:element name="unittitle">
                          <xsl:apply-templates select="unittitle"/>
                      </xsl:element>
                      <xsl:element name="unitdate">
                          <xsl:attribute name="normal">
                              <xsl:apply-templates select="dateF"/>-01-01/<xsl:apply-templates select="dateF"/><xsl:text>-01-01</xsl:text>
                          </xsl:attribute>
                          <xsl:apply-templates select="dateD"/>
                      </xsl:element>
                  </xsl:element>
                  
                  <xsl:element name="scopecontent">
                      <xsl:element name="p">
                          <xsl:apply-templates select="contenu"/>
                      </xsl:element>
                  </xsl:element> 
                  
                  <xsl:element name="custodhist">
                      <xsl:element name="p">
                          <xsl:text>Tables Ardouin, tome </xsl:text><xsl:apply-templates select="tome"/><xsl:text>, page </xsl:text><xsl:apply-templates select="page"/>
                      </xsl:element>
                  </xsl:element>
                  
                  <xsl:element name="controlaccess">
                      <xsl:element name="subject">
                          <xsl:apply-templates select="function"/>
                      </xsl:element>
                  </xsl:element>
              </xsl:element>
          </xsl:for-each>
      </xsl:element>
   </xsl:template>
    
    
</xsl:stylesheet>