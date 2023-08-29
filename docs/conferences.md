---
title: Conferences
summary: The conferences I attended
conferences:
  - name: OWASP Global AppSec
    date: 2023-02-15
    location: Dublin, Ireland
    description: Designed for private and public sector InfoSec professionals, the two-day OWASP conference equips developers, defenders, and advocates to build a more secure web. 
    url: https://dublin.globalappsec.org/
    author: false
  
  - name: NDSS
    date: 2019-02-24
    location: San Diego, CA, USA
    description: The NDSS Symposium is a leading security forum that fosters information exchange among researchers and practitioners of network and distributed system security.
    url: https://www.ndss-symposium.org/ndss2019/
    author: false
  
  - name: CCS
    date: 2018-10-15
    location: Toronto, Canada
    description: The ACM Conference on Computer and Communications Security (CCS) is the flagship annual conference of the Special Interest Group on Security, Audit and Control (SIGSAC) of the Association for Computing Machinery (ACM). The conference brings together information security researchers, practitioners, developers, and users from all over the world to explore cutting-edge ideas and results. 
    url: https://www.sigsac.org/ccs/CCS2018/
    author: false
  
  - name: droidcon
    date: 2018-06-25
    location: Berlin, Germany
    description: droidcon is a commercial conference in Europe, focused on software development for Google's Android smartphone framework. The droidcon conference is the largest Android developer conferences held outside the USA.
    url: https://berlin.droidcon.com/
    author: false
  
  - name: Euro S&P
    date: 2017-04-26
    location: Paris, France
    description:  Since 1980, the IEEE Symposium on Security and Privacy has been the premier forum for presenting developments in computer security and electronic privacy, and for bringing together researchers and practitioners in the field. Following this story of success, IEEE initiated the European Symposium on Security and Privacy (EuroS&P), which is organized every year in a European city.
    url: https://www.ieee-security.org/TC/EuroSP2017/
    author: true
  
  - name: Usenix Security
    date: 2016-08-10
    location: Austin, TX, USA
    description: The USENIX Security Symposium brings together researchers, practitioners, system administrators, system programmers, and others interested in the latest advances in the security and privacy of computer systems and networks.
    url: https://www.usenix.org/conference/usenixsecurity16
    author: true
  
  - name: Euro S&P
    date: 2016-03-21
    location: Saarbrücken, Germany
    description:  Since 1980, the IEEE Symposium on Security and Privacy has been the premier forum for presenting developments in computer security and electronic privacy, and for bringing together researchers and practitioners in the field. Following this story of success, IEEE initiated the European Symposium on Security and Privacy (EuroS&P), which is organized every year in a European city.
    url: https://www.ieee-security.org/TC/EuroSP2016/
    author: false
  
  - name: ACSAC
    date: 2014-12-08
    location: New Orleans, LA, USA
    description: The Annual Computer Security Applications Conference (ACSAC) brings together cutting-edge researchers, with a broad cross-section of security professionals drawn from academia, industry, and government, gathered to present and discuss the latest security results and topics. With peer reviewed technical papers, invited talks, panels, national interest discussions, and workshops, ACSAC continues its core mission of investigating practical solutions for computer and network security technology.
    url: https://www.acsac.org/2014/program-final/
    author: false
  
  - name: PenState University
    date: 2014-12-03
    location: PSU, Pennsylvania, PA
    description: Research Collaboration at PenState University
    url: https://www.psu.edu
  
  - name: parallel
    date: 2013-05-15
    location: Karlsruhe, Germany
    description: Software-conference for parallel and high-performance computing.
    url: https://www.parallelcon.de/2013/
    author: false
  
  - name: Jax
    date: 2012-04-19
    location: Munich, Germany
    description: Conference for Java, architecture- and software-innovation
    url: https://jax.de/
    author: false
---

# Conferences

{% for conference in conferences | sort(attribute='date', reverse = True) %}

!!! note "{{ conference.location }}"

    ## {{ conference.name }} - {{ conference.date | string | truncate(4, true, '') }} {% if conference.author %} :material-book-education-outline: { title="as paper author" } {% endif %}

    > {{ conference.description }}
    >
    > 

    <{{ conference.url }}>

{% endfor %}
