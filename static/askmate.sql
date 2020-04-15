--
-- PostgreSQL database dump
--

-- Dumped from database version 11.7 (Ubuntu 11.7-0ubuntu0.19.10.1)
-- Dumped by pg_dump version 11.7 (Ubuntu 11.7-0ubuntu0.19.10.1)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: answer; Type: TABLE; Schema: public; Owner: dani
--

CREATE TABLE public.answer (
    id integer NOT NULL,
    submission_time timestamp without time zone,
    vote_number integer,
    question_id integer,
    message text,
    image text,
    user_id integer NOT NULL
);


ALTER TABLE public.answer OWNER TO dani;

--
-- Name: answer_id_seq; Type: SEQUENCE; Schema: public; Owner: dani
--

CREATE SEQUENCE public.answer_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.answer_id_seq OWNER TO dani;

--
-- Name: answer_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: dani
--

ALTER SEQUENCE public.answer_id_seq OWNED BY public.answer.id;


--
-- Name: comment; Type: TABLE; Schema: public; Owner: dani
--

CREATE TABLE public.comment (
    id integer NOT NULL,
    question_id integer,
    answer_id integer,
    message text,
    submission_time timestamp without time zone,
    edited_count integer,
    user_id integer NOT NULL
);


ALTER TABLE public.comment OWNER TO dani;

--
-- Name: comment_id_seq; Type: SEQUENCE; Schema: public; Owner: dani
--

CREATE SEQUENCE public.comment_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.comment_id_seq OWNER TO dani;

--
-- Name: comment_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: dani
--

ALTER SEQUENCE public.comment_id_seq OWNED BY public.comment.id;


--
-- Name: question; Type: TABLE; Schema: public; Owner: dani
--

CREATE TABLE public.question (
    id integer NOT NULL,
    submission_time timestamp without time zone,
    view_number integer,
    vote_number integer,
    title text,
    message text,
    image text,
    user_id integer NOT NULL
);


ALTER TABLE public.question OWNER TO dani;

--
-- Name: question_id_seq; Type: SEQUENCE; Schema: public; Owner: dani
--

CREATE SEQUENCE public.question_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.question_id_seq OWNER TO dani;

--
-- Name: question_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: dani
--

ALTER SEQUENCE public.question_id_seq OWNED BY public.question.id;


--
-- Name: question_tag; Type: TABLE; Schema: public; Owner: dani
--

CREATE TABLE public.question_tag (
    question_id integer NOT NULL,
    tag_id integer NOT NULL
);


ALTER TABLE public.question_tag OWNER TO dani;

--
-- Name: tag; Type: TABLE; Schema: public; Owner: dani
--

CREATE TABLE public.tag (
    id integer NOT NULL,
    name text
);


ALTER TABLE public.tag OWNER TO dani;

--
-- Name: tag_id_seq; Type: SEQUENCE; Schema: public; Owner: dani
--

CREATE SEQUENCE public.tag_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.tag_id_seq OWNER TO dani;

--
-- Name: tag_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: dani
--

ALTER SEQUENCE public.tag_id_seq OWNED BY public.tag.id;


--
-- Name: users; Type: TABLE; Schema: public; Owner: dani
--

CREATE TABLE public.users (
    id integer NOT NULL,
    username text NOT NULL,
    password text NOT NULL,
    email text,
    registration_date date,
    reputation integer DEFAULT 0
);


ALTER TABLE public.users OWNER TO dani;

--
-- Name: users_id_seq; Type: SEQUENCE; Schema: public; Owner: dani
--

CREATE SEQUENCE public.users_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.users_id_seq OWNER TO dani;

--
-- Name: users_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: dani
--

ALTER SEQUENCE public.users_id_seq OWNED BY public.users.id;


--
-- Name: answer id; Type: DEFAULT; Schema: public; Owner: dani
--

ALTER TABLE ONLY public.answer ALTER COLUMN id SET DEFAULT nextval('public.answer_id_seq'::regclass);


--
-- Name: comment id; Type: DEFAULT; Schema: public; Owner: dani
--

ALTER TABLE ONLY public.comment ALTER COLUMN id SET DEFAULT nextval('public.comment_id_seq'::regclass);


--
-- Name: question id; Type: DEFAULT; Schema: public; Owner: dani
--

ALTER TABLE ONLY public.question ALTER COLUMN id SET DEFAULT nextval('public.question_id_seq'::regclass);


--
-- Name: tag id; Type: DEFAULT; Schema: public; Owner: dani
--

ALTER TABLE ONLY public.tag ALTER COLUMN id SET DEFAULT nextval('public.tag_id_seq'::regclass);


--
-- Name: users id; Type: DEFAULT; Schema: public; Owner: dani
--

ALTER TABLE ONLY public.users ALTER COLUMN id SET DEFAULT nextval('public.users_id_seq'::regclass);


--
-- Data for Name: answer; Type: TABLE DATA; Schema: public; Owner: dani
--

COPY public.answer (id, submission_time, vote_number, question_id, message, image, user_id) FROM stdin;
20	2020-04-15 21:37:10	64	19	yu du	\N	1
22	2020-04-15 22:23:21	0	20	Why is that man, you should spill it	\N	1
\.


--
-- Data for Name: comment; Type: TABLE DATA; Schema: public; Owner: dani
--

COPY public.comment (id, question_id, answer_id, message, submission_time, edited_count, user_id) FROM stdin;
\.


--
-- Data for Name: question; Type: TABLE DATA; Schema: public; Owner: dani
--

COPY public.question (id, submission_time, view_number, vote_number, title, message, image, user_id) FROM stdin;
19	2020-04-15 19:24:37	42	8	Yo	Eat it br	\N	1
20	2020-04-15 22:21:13	3	0	Yo homies	I cant eat my chickensoup	\N	4
\.


--
-- Data for Name: question_tag; Type: TABLE DATA; Schema: public; Owner: dani
--

COPY public.question_tag (question_id, tag_id) FROM stdin;
19	2
20	1
\.


--
-- Data for Name: tag; Type: TABLE DATA; Schema: public; Owner: dani
--

COPY public.tag (id, name) FROM stdin;
1	python
2	sql
3	css
\.


--
-- Data for Name: users; Type: TABLE DATA; Schema: public; Owner: dani
--

COPY public.users (id, username, password, email, registration_date, reputation) FROM stdin;
2	kiskutyika	$2b$12$j8pSzmymLfnIWudKKKI0HeY.UTj/jLwxZHJAYj1h5uNYgc0g8tmj6	kiskutyika@kutyasz.com	\N	0
3	tester	$2b$12$FlhqlEgTxjzfA38YB71LJ.WK7ja3diaBsou8dUsIgu6f2.FsnkHj2	test@er.com	2020-04-15	0
1	Bela	$2b$12$ft//lfRMUMHkhwrgBjLdpeGf/Su.o9rKUCLbrfBwr0.di3ZbfesU6	john@hoe.com	\N	636
4	testerr	$2b$12$3yrLX3CFeRDBepsgBdHYdu/0HGC5YHAfo9KUQQ7hA0dnbjPasCj8y	test@err.com	2020-04-15	0
\.


--
-- Name: answer_id_seq; Type: SEQUENCE SET; Schema: public; Owner: dani
--

SELECT pg_catalog.setval('public.answer_id_seq', 22, true);


--
-- Name: comment_id_seq; Type: SEQUENCE SET; Schema: public; Owner: dani
--

SELECT pg_catalog.setval('public.comment_id_seq', 24, true);


--
-- Name: question_id_seq; Type: SEQUENCE SET; Schema: public; Owner: dani
--

SELECT pg_catalog.setval('public.question_id_seq', 20, true);


--
-- Name: tag_id_seq; Type: SEQUENCE SET; Schema: public; Owner: dani
--

SELECT pg_catalog.setval('public.tag_id_seq', 3, true);


--
-- Name: users_id_seq; Type: SEQUENCE SET; Schema: public; Owner: dani
--

SELECT pg_catalog.setval('public.users_id_seq', 4, true);


--
-- Name: answer pk_answer_id; Type: CONSTRAINT; Schema: public; Owner: dani
--

ALTER TABLE ONLY public.answer
    ADD CONSTRAINT pk_answer_id PRIMARY KEY (id);


--
-- Name: comment pk_comment_id; Type: CONSTRAINT; Schema: public; Owner: dani
--

ALTER TABLE ONLY public.comment
    ADD CONSTRAINT pk_comment_id PRIMARY KEY (id);


--
-- Name: question pk_question_id; Type: CONSTRAINT; Schema: public; Owner: dani
--

ALTER TABLE ONLY public.question
    ADD CONSTRAINT pk_question_id PRIMARY KEY (id);


--
-- Name: question_tag pk_question_tag_id; Type: CONSTRAINT; Schema: public; Owner: dani
--

ALTER TABLE ONLY public.question_tag
    ADD CONSTRAINT pk_question_tag_id PRIMARY KEY (question_id, tag_id);


--
-- Name: tag pk_tag_id; Type: CONSTRAINT; Schema: public; Owner: dani
--

ALTER TABLE ONLY public.tag
    ADD CONSTRAINT pk_tag_id PRIMARY KEY (id);


--
-- Name: users users_pk; Type: CONSTRAINT; Schema: public; Owner: dani
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_pk PRIMARY KEY (id);


--
-- Name: question_user_id_uindex_2; Type: INDEX; Schema: public; Owner: dani
--

CREATE UNIQUE INDEX question_user_id_uindex_2 ON public.question USING btree (user_id);


--
-- Name: users_email_uindex; Type: INDEX; Schema: public; Owner: dani
--

CREATE UNIQUE INDEX users_email_uindex ON public.users USING btree (email);


--
-- Name: users_id_uindex; Type: INDEX; Schema: public; Owner: dani
--

CREATE UNIQUE INDEX users_id_uindex ON public.users USING btree (id);


--
-- Name: users_username_uindex; Type: INDEX; Schema: public; Owner: dani
--

CREATE UNIQUE INDEX users_username_uindex ON public.users USING btree (username);


--
-- Name: answer answer_users_id_fk; Type: FK CONSTRAINT; Schema: public; Owner: dani
--

ALTER TABLE ONLY public.answer
    ADD CONSTRAINT answer_users_id_fk FOREIGN KEY (user_id) REFERENCES public.users(id) ON DELETE CASCADE;


--
-- Name: comment comment_users_id_fk; Type: FK CONSTRAINT; Schema: public; Owner: dani
--

ALTER TABLE ONLY public.comment
    ADD CONSTRAINT comment_users_id_fk FOREIGN KEY (user_id) REFERENCES public.users(id) ON DELETE CASCADE;


--
-- Name: comment fk_answer_id; Type: FK CONSTRAINT; Schema: public; Owner: dani
--

ALTER TABLE ONLY public.comment
    ADD CONSTRAINT fk_answer_id FOREIGN KEY (answer_id) REFERENCES public.answer(id);


--
-- Name: answer fk_question_id; Type: FK CONSTRAINT; Schema: public; Owner: dani
--

ALTER TABLE ONLY public.answer
    ADD CONSTRAINT fk_question_id FOREIGN KEY (question_id) REFERENCES public.question(id);


--
-- Name: question_tag fk_question_id; Type: FK CONSTRAINT; Schema: public; Owner: dani
--

ALTER TABLE ONLY public.question_tag
    ADD CONSTRAINT fk_question_id FOREIGN KEY (question_id) REFERENCES public.question(id);


--
-- Name: comment fk_question_id; Type: FK CONSTRAINT; Schema: public; Owner: dani
--

ALTER TABLE ONLY public.comment
    ADD CONSTRAINT fk_question_id FOREIGN KEY (question_id) REFERENCES public.question(id);


--
-- Name: question_tag fk_tag_id; Type: FK CONSTRAINT; Schema: public; Owner: dani
--

ALTER TABLE ONLY public.question_tag
    ADD CONSTRAINT fk_tag_id FOREIGN KEY (tag_id) REFERENCES public.tag(id);


--
-- Name: question question_users_id_fk; Type: FK CONSTRAINT; Schema: public; Owner: dani
--

ALTER TABLE ONLY public.question
    ADD CONSTRAINT question_users_id_fk FOREIGN KEY (user_id) REFERENCES public.users(id) ON DELETE CASCADE;


--
-- Name: question question_users_id_fk_2; Type: FK CONSTRAINT; Schema: public; Owner: dani
--

ALTER TABLE ONLY public.question
    ADD CONSTRAINT question_users_id_fk_2 FOREIGN KEY (user_id) REFERENCES public.users(id);


--
-- PostgreSQL database dump complete
--

